from redis import asyncio as aioredis
import os

async def sys_cache() -> aioredis.Redis:
    # # redis connection
    # redis_connection = aioredis.Connection(host=os.getenv('REDIS_HOST', '127.0.0.1'),
    #                                        port=os.getenv('REDIS_PORT', '6379',),
    #                                        username=os.getenv('REDIS_USER', 'default'),
    #                                        password=os.getenv('REDIS_PASSWORD'),
    #                                        db=os.getenv('REDIS_DB', '0')
    #                                        )
    # reids connection pool
    connection_pool = aioredis.ConnectionPool(host=os.getenv('REDIS_HOST', '127.0.0.1'),
                                           port=os.getenv('REDIS_PORT', '6379',),
                                           username=os.getenv('REDIS_USER', 'default'),
                                           password=os.getenv('REDIS_PASSWORD'),
                                           db=os.getenv('REDIS_DB', '0')
                                           )
    print(connection_pool)
    return aioredis.Redis(connection_pool=connection_pool)