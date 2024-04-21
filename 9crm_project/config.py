"""
应用个性化配置
"""
import os
from typing import List
from dotenv import load_dotenv

class Config:

    # 加载环境变量
    load_dotenv('.env', override=True)

    # APP信息
    APP_DEBUG: bool = False
    APP_TITLE: str = 'fastapi-demo'
    APP_DESCRIPTION: str = 'fastapi项目demo'
    APP_VERSION: str = '0.0.1'

    # 静态资源路径
    STATIC_DIR = os.path.join(os.getcwd(), 'static')
    TEMPLATE_DIR = os.path.join(STATIC_DIR, 'templates')

    # 访问地址，端口
    HOST = '127.0.0.1'
    PORT = 8000

    # 跨域请求
    COR_ORIGINS: List[str] = ['*']
    COR_METHODS: List[str] = ['*']
    COR_HEADERS: List[str] = ['*']
    COR_CREDENTIALS: bool = True

setting = Config()