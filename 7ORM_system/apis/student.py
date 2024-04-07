from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from models import *
router = APIRouter()
templates = Jinja2Templates('templates')

@router.get('')
async def students(request: Request):
    """查看所有students的姓名和学号"""
    stus = await Student.all().values('name', 'sn')
    return templates.TemplateResponse(request, 'index.html', context={'stus': stus})

@router.get('/{sn}')
async def student(sn: int):
    """查看学号 为 sn的学生"""
    stu = await Student.get(sn=sn)
    return stu

@router.post('')
async def student():
    """添加student"""

@router.put('/id')
async def student(id: int):
    """修改student_id = id的学生信息"""

@router.delete('/id')
async def student(id: int):
    """删除student_id = id的学生信息"""
