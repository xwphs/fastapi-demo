"""
中间件
"""
from starlette.types import ASGIApp, Scope, Receive, Send, Message
import time
from fastapi import Request
from core.utils import random_str
from starlette.datastructures import MutableHeaders

class MyMiddleWare:
    def __init__(self, app: ASGIApp):
        self.app = app
    
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        request = Request(scope, receive, send)
        if not request.session.get('session'):
            request.session.setdefault('session', random_str())

        async def send_warpper(msg: Message):
            process_time = time.time() - start_time
            if msg['type'] == 'http.response.start':
                headers = MutableHeaders(scope=msg)
                headers.append('X-Process-Time', str(process_time))
            await send(msg)
        await self.app(scope, receive, send_warpper)
        