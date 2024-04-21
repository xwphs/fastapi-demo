"""
fastapi异常处理
"""
from fastapi import Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

async def http_err_handler(_: Request, exc: HTTPException):
    return JSONResponse({"code": exc.status_code,
                         "message": exc.detail,
                         "data": exc.detail},
                         status_code=exc.status_code)

async def http422_err_handler(_: Request, exc: Union[RequestValidationError, ValidationError]):
    return JSONResponse({"code": status.HTTP_422_UNPROCESSABLE_ENTITY,
                         "message": f'参数校验错误{exc.errors()}',
                         "data": exc.errors()})

class UvicornException(Exception):
    def __init__(self, code, errmsg, data={}):
        self.code = code
        self.errmsg = errmsg
        self.data = data

async def uvicorn_exception_handler(_: Request, exc: UvicornException):
    return JSONResponse({
        "code": exc.code,
        "message": exc.errmsg,
        "data": exc.data
    })