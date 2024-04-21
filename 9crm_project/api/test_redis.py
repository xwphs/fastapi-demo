from fastapi import Request
from redis.asyncio import Redis

async def days(req: Request, day: int):
    cache: Redis = req.app.state.cache
    await cache.set('day', day)
    return {'message': 'success', 'day': day}
