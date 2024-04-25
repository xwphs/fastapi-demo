from tortoise.models import Model
from tortoise import fields

# class User(Model):
#     username = fields.CharField(max_length=20, description="用户名")
#     type = fields.BooleanField(default=False, description="True: 超级管理员, False: 普通管理员")
#     password = fields.CharField(max_length=255)
#     nickname = fields.CharField(max_length=255, null=True, description='昵称')
#     u_phone = fields.CharField(max_length=11, null=True, description='手机号')
#     u_email = fields.CharField(max_length=255, null=True, description='邮箱')
#     u_status = fields.IntField(default=0, description='0未激活 1正常 2禁用')
#     avatar = fields.CharField(max_length=255, null=True, description='头像')
#     sex = fields.IntField(default=0, null=True, description='0未知 1男 2女')
#     remarks = fields.CharField(max_length=30, null=True, description='备注')
#     client_host = fields.CharField(max_length=30, null=True, description='访问ip')
#     create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
#     update_time = fields.DatetimeField(auto_now=True, description='更新时间')

#     class Meta:
#         table_description = "用户"

# 设计一个RBAC功能
class TimestampMixin(Model):
    create_time = fields.DatetimeField(auto_now_add=True, description='创建时间')
    update_time = fields.DatetimeField(auto_now=True, description='更新时间')

    class Meta:
        table = None

class Role(TimestampMixin):
    role_name = fields.CharField(20, description='角色名称')
    user = fields.ManyToManyField('models.User', related_name='role')
    access = fields.ManyToManyField('models.Access', related_name='role')
    role_status = fields.BooleanField(default=False, description='True:启用 False:禁用')
    role_desc = fields.CharField(255, null=True, description='角色描述')

    class Meta:
        table_description = '角色表'

class User(TimestampMixin):
    role: fields.ManyToManyRelation[Role]
    username = fields.CharField(20,description='用户名')
    user_type = fields.IntField(default=2, description='0:超级管理员 1:管理员 2:普通用户')
    password = fields.CharField(255, description='密码')
    gender = fields.IntField(null=True, description='0男 1女')
    nickname = fields.CharField(30, null=True, description='昵称')
    phone = fields.CharField(11, null=True, description='手机号')
    email = fields.CharField(20, null=True)
    user_status = fields.IntField(default=0, description='0未激活 1正常 2禁用')
    avatar = fields.CharField(255, null=True, description='头像')
    remark = fields.CharField(255, null=True, description='备注')
    client_host = fields.CharField(20, null=True, description='访问ip')
    
    class Meta:
        table_description = '用户表'

class Access(TimestampMixin):
    role: fields.ManyToManyRelation[Role]
    access_name = fields.CharField(20, description='权限名称')
    parent_id = fields.IntField(default=0, description='父id')
    scopes = fields.CharField(255, null=True, description='权限范围')
    access_desc = fields.CharField(255, null=True, description='权限描述')
    menu_icon = fields.CharField(255, null=True, description='菜单图标')
    is_check = fields.BooleanField(default=False, description='True验证 False不验证')
    is_menu = fields.BooleanField(default=False, description='是否为菜单 True菜单 False不是菜单')

    class Meta:
        table_description = '权限表'

class AccessLog(TimestampMixin):
    user_id = fields.IntField(description='用户id')
    target_url = fields.CharField(255, null=True)
    user_agent = fields.CharField(255, null=True)
    request_params = fields.JSONField(null=True, description='get|post')
    ip = fields.CharField(20, null=True)
    note = fields.CharField(255, null=True, description='备注')

    class Meta:
        table_description='用户操作记录表'
        table = 'access_log'