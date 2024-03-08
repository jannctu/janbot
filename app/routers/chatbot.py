from fastapi import APIRouter, status, Depends
from app.dto.chatbot.chatbot_handle import HandleChatbotInput
from app.services.chatbot import ChatbotService

router = APIRouter(prefix="/chatbot", tags=["chatbot"])


@router.get("/health")
def health_check():
    return {"message": "JanBot OK"}


@router.post("/", status_code=status.HTTP_200_OK)
def handle(
        payload: HandleChatbotInput,
        chatbot_service: ChatbotService = Depends()
):
    return chatbot_service.handle(payload)
