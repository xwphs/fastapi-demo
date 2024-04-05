from fastapi import APIRouter, Form

router = APIRouter()

@router.post('/register')
async def register(username: str =Form(), password: str =Form()):
    """使用x-www-form-urlencoded方式接受请求"""
    print(f'username: {username}, password: {password}')
    return {"username": username}