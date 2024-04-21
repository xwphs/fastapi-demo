from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
import os

DB_ORM_CONFIG={
    'connections': {
        # Dict format for connection
        'db1': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': os.getenv('MYSQL_HOST', '127.0.0.1'),
                'port': int(os.getenv('MYSQL_PORT', 3306)),
                'user': os.getenv('MYSQL_USER', 'root'),
                'password': os.getenv('MYSQL_PASSWORD'),
                'database': os.getenv('MYSQL_DB'),
            }
        }
    },
    'apps': {
        'models': {
            'models': ['models.base'],
            # If no default_connection specified, defaults to 'default'
            'default_connection': 'db1',
        }
    },
    'timezone': 'Asia/Shanghai'
}

async def registe_mysql(app: FastAPI):
    register_tortoise(app, config=DB_ORM_CONFIG, generate_schemas=True)
