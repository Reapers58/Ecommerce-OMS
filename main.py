from fastapi import FastAPI
from config.settings import settings
from src.router import router 

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="E-commerce Order Management System API"
)

app.include_router(router)