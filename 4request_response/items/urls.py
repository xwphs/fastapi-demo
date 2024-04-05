from fastapi import APIRouter, Request

router = APIRouter()

def message(req: Request):
    m = {"host": req.client.host,
         "url": req.url,
         "agent": req.headers.get('user-agent'),
         "cookie": req.cookies}
    return m

@router.get('/items')
async def info(request: Request):
    return message(request)