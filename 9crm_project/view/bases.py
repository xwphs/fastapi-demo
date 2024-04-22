"""
视图路由
"""
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from models.base import User
view_router = APIRouter()

# session 和 cookie
@view_router.get('/home')
async def home(req: Request):
    cookie = req.cookies.get('session_id')
    session = req.session.get('session')
    templates: Jinja2Templates = req.app.state.views
    return templates.TemplateResponse(req, 'index.html', {'cookie': cookie, 'session': session})

@view_router.get('/reg')
async def reg_page(req: Request):
    templates: Jinja2Templates = req.app.state.views
    return templates.TemplateResponse(req, 'reg_page.html')

@view_router.post('/reg/form')
async def reg_result_page(req: Request, username: str = Form(...), password: str = Form(...)):
    # 插入用户信息
    await User.create(username=username, password=password)
    templates: Jinja2Templates = req.app.state.views
    return templates.TemplateResponse(req, 'reg_result.html', context={'username': username, 'password': password})
