from fastapi import FastAPI
from user.urls import router as router1
from jobs.urls import router as router2
from vip.urls import router as router3
from register.urls import router as router4
from uploadFile.urls import router as router5
from items.urls import router as router6
import uvicorn
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'))    # 静态文件
app.include_router(router1, tags=['Path parameter'])
app.include_router(router2, tags=['Query parameter'])
app.include_router(router3, tags=['Request body'])
app.include_router(router4, tags=['Form 表单'])
app.include_router(router5, tags=['Upload file'])
app.include_router(router6, tags=['Request对象'])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8090, reload=True)