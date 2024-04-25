from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
import jwt
import datetime
from config import setting
from fastapi import Request, Depends, HTTPException
from fastapi.security import SecurityScopes
from starlette import status
from pydantic import ValidationError
from jwt import PyJWTError
from models.base import User, Access


oauth2 = OAuth2PasswordBearer("")

def creat_access_token(data: dict)-> str:
    token_data = data.copy()
    expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=setting.JWT_TOKEN_EXPIRE_MINUTES)
    token_data.update({'exp': expire})
    jwt_token = jwt.encode(payload=token_data, key=setting.JWT_SECRET_KEY, algorithm=setting.JWT_ALGORITHM)
    return jwt_token

async def check_permission(req: Request, security_scopes: SecurityScopes, token=Depends(oauth2)):
    # 验证token
    # print('token ', token)
    # print('scopes',security_scopes.scopes)
    authorization = req.headers.get('Authorization')
    scheme, param = get_authorization_scheme_param(authorization)
    if not authorization or scheme.lower() != 'bearer':
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Not Authenticated',
            headers={'WWW-AUTHTICATE': 'Bearer'}
        )
    
    # 取出token
    token = param
    try:
        # token解密
        payload: dict = jwt.decode(token, setting.JWT_SECRET_KEY, algorithms=[setting.JWT_ALGORITHM])
        if payload:
            user_id = payload.get('user_id', None)
            user_type = payload.get('user_type', None)
            # 无效用户信息
            if user_id is None or user_type is None:
                credentials_exception = HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='无效凭证',
                    headers={'WWW-Authenticate': f"Bearer {token}"}
                )
                raise credentials_exception
        else:
            raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='无效凭证',
                    headers={'WWW-Authenticate': f"Bearer {token}"}
                )
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='凭证已过期',
            headers={'WWW-Authenticate': f'Bearer {token}'}
        )
    except (jwt.InvalidTokenError, PyJWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='无效凭证',
            headers={'WWW-Authenticate': f'Bearer {token}'}
        )
    except Exception:
        # 未知异常
        pass

    # 验证权限
    # 用户是否有效，是否被禁用
    check_user = await User.get_or_none(pk=user_id)
    if not check_user or check_user.user_status != 1:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='用户不存在或已经被禁用',
            headers={'WWW-Authenticate': f'Bearer {token}'}
        )
    # 是否设置了权限域
    if security_scopes.scopes:
        # print('current scopes: ', security_scopes.scopes)
        # 非超级管理员需要验证
        if user_type:
            is_pass = await Access.get_or_none(role__user__id=user_id,
                                         is_check=True,
                                         scopes__in=set(security_scopes.scopes),
                                         role__role_status=True)
            if not is_pass:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Not Permissions',
                    headers={'scopes': security_scopes.scope_str}
                )
            # 查询用户所有scopes
            scopes = await Access.filter(role__user__id=user_id, is_check=True, role__role_status=True).values_list('scopes')
            req.state.scopes = scopes
    # 缓存用户id和用户类型
    req.state.user_id = user_id
    req.state.user_type = user_type
