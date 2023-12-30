from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from sqlmodel import SQLModel
from db import engine
from routers import router
from auth import router as auth_router

@asynccontextmanager
async def db_setup(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=db_setup)
app.include_router(auth_router)
app.include_router(router)



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
