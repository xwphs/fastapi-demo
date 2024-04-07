from fastapi import FastAPI
import uvicorn
from apis.student import router as student
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(student, prefix='/student', tags=['学生选课系统'])
## 映射models.py中类到数据库中的表
register_tortoise(app=app,db_url="mysql://root:xwp1234567@117.29.10.233:3306/tortoise_orm", modules={'models': ['models']}, generate_schemas=True)


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)