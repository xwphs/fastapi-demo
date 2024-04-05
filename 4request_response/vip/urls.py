from fastapi import APIRouter
from pydantic import BaseModel, validator, Field
from datetime import date
from typing import List, Optional

router = APIRouter()

class Addr(BaseModel):
    prinvince: str
    city: str

class Vip(BaseModel):
    id: int
    name: str
    age: int = Field(gt=0, le=100)
    birth: Optional[date] = None
    friends: List[int]
    addr: Optional[Addr] = None

# 校验name字段是否为纯字母，不包含数字
    @validator('name')
    def name_must_xwp(cls, value):
        assert value.isalpha(), "name must be ahpha"
        return value
    
class Data(BaseModel):
    data: List[Vip]

@router.post('/vip')
async def vip(v: Vip):
    return v

@router.post('/data')
async def vip(d: Data):
    return d