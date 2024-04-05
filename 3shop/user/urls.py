from fastapi import APIRouter

router = APIRouter()

@router.get('/vip')
async def vip():
    return {"username": "肖维鹏",
            "VIP": 10}

@router.get('/user')
async def user():
    return {"userlist": ["lenyu", "xwp", "uzi"]}
