from fastapi.routing import APIRouter
from app.routers import chatbot

api_router = APIRouter()

api_router.include_router(chatbot.router)
