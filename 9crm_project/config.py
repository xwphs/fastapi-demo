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

    # Session
    SECRET_KEY='session'
    SESSION_COOKIE = 'session_id'
    MAX_AGE = 7 * 24 * 60 * 60

    # JWT
    JWT_TOKEN_EXPIRE_MINUTES = 24 * 60
    JWT_SECRET_KEY = 'xwphs1234afaafagasfare93qags3'
    JWT_ALGORITHM = 'HS256'

setting = Config()