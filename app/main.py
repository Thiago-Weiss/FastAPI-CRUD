from fastapi import FastAPI
from contextlib import asynccontextmanager


from app.services import create_db_and_tables
from app.api import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicialização (startup)
    create_db_and_tables()
    yield



app = FastAPI(
        lifespan=lifespan,
    )

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


