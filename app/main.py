from fastapi import FastAPI
from app.routers import task, user
from app import *
app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user.router)
app.include_router(task.router)





#                          python -m uvicorn app.main:app