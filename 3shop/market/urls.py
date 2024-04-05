from fastapi import APIRouter

router = APIRouter()

@router.get('/bed')
async def bed():
    return 'Bed count: 3'

@router.get('/clothes')
async def clothes():
    return 'Clothes count: 20'