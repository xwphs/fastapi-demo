from fastapi import APIRouter
from typing import Optional, Union

router = APIRouter()

@router.get('/job/{kw}')
async def job(kw, gj: Union[str, None]=None, xl: Optional[str]=None):
    return {
        "keyword": kw,
        "工作经验": gj,
        "学历": xl
    }