from tortoise.models import Model
from tortoise import fields

class User(Model):
    username = fields.CharField(max_length=20, description="用户名")
    type = fields.BooleanField(default=False, description="True: 超级管理员, False: 普通管理员")
    password = fields.CharField(max_length=255)
    nickname = fields.CharField(max_length=255, null=True, description='昵称')
    u_phone = fields.CharField(max_length=11, null=True, description='手机号')
    u_email = fields.CharField(max_length=255, null=True, description='邮箱')
    u_status = fields.IntField(default=0, description='0未激活 1正常 2禁用')
    avatar = fields.CharField(max_length=255, null=True, description='头像')
    sex = fields.IntField(default=0, null=True, description='0未知 1男 2女')
    remarks = fields.CharField(max_length=30, null=True, description='备注')
    client_host = fields.CharField(max_length=30, null=True, description='访问ip')
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description='更新时间')

    class Meta:
        table_description = "用户"