from fastapi import FastAPI, Request,Response
from typing import Callable, Awaitable
import uvicorn
from apis.urls import router as index
import time

app = FastAPI()

# 中间件的执行顺序是代码越靠前的，越靠近业务代码。即请求先到add_process_time_header,再到test_mw
@app.middleware('http')
async def test_mw(request: Request, call_next: Callable[..., Awaitable[Response]]):
    print('test_mw in ...')
    response = await call_next(request)
    print('test_mw out ...')
    return response

@app.middleware('http')
async def add_process_time_header(request: Request, call_next: Callable[..., Awaitable[Response]]):
    start = time.time()
    print('add_process_time_header in ...')
    response = await call_next(request)
    response.headers['Process-Time'] = str(time.time() - start)
    print('add_process_time_header out ...')
    return response

app.include_router(index, tags=['Testing middleware'])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)