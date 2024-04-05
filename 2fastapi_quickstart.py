from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/home")
async def home():
    return {"user_id": 101, "username": "肖维鹏"}

@app.get("/users")
async def user():
    return {"userlist": ["xwp", "lenyu", "污渍"]}

if __name__ == '__main__':
    uvicorn.run('2fastapi_quickstart:app', port=8080, reload=True)