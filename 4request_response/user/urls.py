from fastapi import APIRouter

router = APIRouter()

@router.get('/user/1')
async def user():
    return {"username": "admin"}

@router.get('/user/{id}')
async def user(id: int):
    return {"message": f"查询user id: {id}"}

@router.delete('/user/{id}')
async def user(id: int):
    return {"message": f"id {id} 已删除"}
