from fastapi import APIRouter, Request
from api.test_redis import days
from redis.asyncio import Redis

api_router = APIRouter(prefix='/v1')

@api_router.get('')
async def base():
    return "fastapi demo"

# test redis 
api_router.post('/days')(days)

@api_router.get('/days')
async def days(req: Request):
    cache: Redis = req.app.state.cache
    day = await cache.get('day')
    return {'message': 'success', 'day': day}