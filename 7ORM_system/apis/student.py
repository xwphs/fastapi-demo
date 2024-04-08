from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException
from typing import List
from tortoise import exceptions
from pydantic import BaseModel, validator
from models import *
router = APIRouter()
templates = Jinja2Templates('templates')

class StudentIn(BaseModel):
    name: str
    pwd: str
    sn: int
    clas_id: int
    courses: List[int] = []

@router.get('')
async def students(request: Request):
    """查看所有students的姓名和学号"""
    stus = await Student.all().values('name', 'sn')
    return templates.TemplateResponse(request, 'index.html', context={'stus': stus})

@router.get('/{sn}')
async def student(sn: int):
    """查看学号 为 sn的学生"""
    try:
        stu = await Student.get(sn=sn)
        return stu
    except exceptions.DoesNotExist as e:
        return {"Err message": f"学号为{sn}的学生不存在"}
    
@router.post('')
async def student(stu_in: StudentIn):
    """添加student"""
    stu = await Student.create(name=stu_in.name, pwd=stu_in.pwd, sn=stu_in.sn, clas_id=stu_in.clas_id)   # 这里不需要多对多的字段，因为它会单独生成一张中间表。
    # 因为many_to_many关系会生成一个中间表，这个在models中没有体现，所以只能通过 实例.course来添加
    queryed_courses = await Course.filter(id__in=stu_in.courses)
    await stu.course.add(*queryed_courses)
    return stu

@router.put('/{sn}')
async def student(sn: int, stu_in: StudentIn):
    """修改学号为sn的学生信息"""
    try:
        stu = await Student.get(sn=sn)
    except exceptions.DoesNotExist:
        return {"Err message": f"学号为{sn}的学生不存在"}
    updated_student = stu.update_from_dict(stu_in.model_dump(exclude='courses'))        # 该update方法暂无自动保存，所以修改后保存下.
    await stu.save()
    queried_course = await Course.filter(id__in=stu_in.courses)
    await stu.course.clear()
    await stu.course.add(*queried_course)
    return updated_student

@router.delete('/{sn}')
async def student(sn: int):
    """删除学号为sn的学生信息"""
    deleted_student = await Student.filter(sn=sn).delete()
    if not deleted_student:
        raise HTTPException(status_code=404, detail=f'Student 学号{sn} not found')
    return {"message": "删除成功"}
