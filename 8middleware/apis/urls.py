from fastapi import APIRouter

router = APIRouter()

@router.get("/index")
async def index():
    print("index func...")
    return {"message": "testing"}