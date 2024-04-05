from fastapi import FastAPI
from market.urls import router as market
from user.urls import router as user
import uvicorn

app = FastAPI()
app.include_router(market, prefix='/shop', tags=['market'])
app.include_router(user, prefix='/shop', tags=['user'])

if __name__ == '__main__':
    uvicorn.run('main:app', port=8080, reload=True)