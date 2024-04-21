from fastapi import FastAPI, HTTPException
from config import setting
from core.events import startup, shutdown
from core.exception import http_err_handler, http422_err_handler, UvicornException, uvicorn_exception_handler
from fastapi.exceptions import RequestValidationError
from core.router import all_router
from core.middleware import MyMiddleWare
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(
    debug=setting.APP_DEBUG,
    title=setting.APP_TITLE,
    description=setting.APP_DESCRIPTION,
    version=setting.APP_VERSION
)

# 事件监听
app.add_event_handler('startup', startup(app))
app.add_event_handler('shutdown', shutdown(app))

# 异常处理
app.add_exception_handler(HTTPException, http_err_handler)
app.add_exception_handler(RequestValidationError, http422_err_handler)
app.add_exception_handler(UvicornException, uvicorn_exception_handler)

# 路由
app.include_router(all_router)

# 中间件
app.add_middleware(MyMiddleWare)
app.add_middleware(SessionMiddleware,
                   secret_key='session',
                   session_cookie='f_id')
app.add_middleware(CORSMiddleware,
                   allow_origins=setting.COR_ORIGINS,
                   allow_methods=setting.COR_METHODS,
                   allow_headers=setting.COR_HEADERS,
                   allow_credentials=setting.COR_CREDENTIALS)

# 静态资源目录
app.mount('/static', StaticFiles(directory=setting.STATIC_DIR))
app.state.views = Jinja2Templates(directory=setting.TEMPLATE_DIR)

# 启动
if __name__ == '__main__':
    uvicorn.run('app:app', host=setting.HOST, port=setting.PORT, reload=True)