from tortoise.models import Model
from tortoise import fields


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(32, description='学生姓名')
    pwd = fields.CharField(32, description='密码')
    sn = fields.IntField(index=True, description='学号')
    # 一对多关系
    clas = fields.ForeignKeyField('models.Clas', related_name='students')
    # 多对多关系
    course = fields.ManyToManyField('models.Course', related_name='students')

class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(32, description='班级名称')

class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(32, description='课程名称')
    # 一对多关系(假设一个教师可以教多个课程)
    teacher = fields.ForeignKeyField('models.Teacher', related_name='courses')

class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(32, description='教师姓名')
    tn = fields.IntField(description='教师编号')
    pwd = fields.CharField(32, description='密码')
