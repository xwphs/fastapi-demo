from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app =  FastAPI()
templates = Jinja2Templates('templates')

@app.get('/index', tags=['主页'], description='主页')
async def index(request: Request):
    name = '杨俊杰'; age = 19
    stars = ['药水哥', 'giao哥', '宇将军', '陈泽']
    movies = {'av': ['日韩', '欧美', '国产', '无码'], 'cartoon': ['熊出没', '喜羊羊与灰太狼', '迪迦奥特曼', '七龙珠']}
    return templates.TemplateResponse(request, 'index.html', context={"name": name, "age": age, "stars": stars, "movies": movies})

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)
    