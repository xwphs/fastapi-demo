"""
fastapi事件监听
"""
from fastapi import FastAPI
from typing import Callable
from database.mysql import registe_mysql
from database.redis import sys_cache
def startup(app: FastAPI)-> Callable:
    async def app_start():
        print('应用启动')
        # 注册mysql
        await registe_mysql(app)
        # 注入缓存到app state
        # app.state.cache = await sys_cache()
    return app_start

def shutdown(app: FastAPI) ->Callable:
    async def app_stop():
        print('应用停止')
        pass
    return app_stop
