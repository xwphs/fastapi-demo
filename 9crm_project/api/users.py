from fastapi import APIRouter, Security, Request
from pydantic import BaseModel, Field
from models import base
from core.response import success, fail
from core.auth import creat_access_token, check_permission

user_router = APIRouter()

class User(BaseModel):
    username: str = Field(max_length=20)
    password: str = Field(min_length=5)
    user_type: int = 2

class Account(BaseModel):
    username: str
    password: str

@user_router.post('/login')
async def login(account: Account):
    """
    返回一个jwt token
    """
    # 判断用户是否存在，密码校验
    user = await base.User.get_or_none(username=account.username)
    if not user:
        return fail(msg=f'用户{account.username}密码校验错误')
    elif account.password != user.password:
        return fail(msg=f'用户{account.username}密码校验错误')
    elif user.user_status == 2:
        return fail(msg=f'用户{account.username}被禁用')
    else:
        pass
    jwt_data = {
        'user_id': user.pk,
        'user_type': user.user_type
    }
    token = creat_access_token(jwt_data)
    return success(msg='登录成功', data={'token': token})


@user_router.get('/user/info', dependencies=[Security(dependency=check_permission)])
async def info(req: Request):
    cur_user = await base.User.get(pk=req.state.user_id)
    return success(msg='用户信息', data=cur_user)


@user_router.get('/user/{id}', dependencies=[Security(dependency=check_permission, scopes=['read'])])
async def user(id: int):
    user = await base.User.get_or_none(pk=id)
    if not user:
        return fail(code=404, msg=f'用户id{id}不存在')
    return success(msg='用户信息', data=user)

@user_router.post('/user', dependencies=[Security(dependency=check_permission, scopes=['write'])])
async def user(user: User):
    user = await base.User.create(**user.model_dump())
    if not user:
        return fail(msg='创建失败')
    return success(msg='创建成功')

@user_router.delete('/user/{id}', dependencies=[Security(dependency=check_permission, scopes=['write'])])
async def user(id: int):
    result = await base.User.filter(pk=id).delete()
    if not result:
        return fail(msg='删除失败')
    return success(msg='删除成功')

@user_router.get('/user_role')
async def user_role(id: int):
    # 查询用户的角色
    roles = await base.Role.filter(user__id=id).values('role_name')
    # 查询用户的所有权限
    access = await base.Access.filter(role__user__id=id).values('access_name', 'scopes')
    
    data = {
        'roles': roles,
        'access': access
    }
    return success(msg='用户权限', data=data)
