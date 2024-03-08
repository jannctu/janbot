from app.dto.chatbot.chatbot_handle import HandleChatbotInput, HandleChatbotOutput
from app.helpers.chatgpt import ChatGptHelper
from fastapi import Depends


class ChatbotService:
    def __init__(self, chatgpt_helper: ChatGptHelper = Depends()) -> None:
        self.chatgpt_helper = chatgpt_helper

    def handle(self, handle_input: HandleChatbotInput) -> HandleChatbotOutput:
        response = self.chatgpt_helper.handle(message=handle_input.message)

        return HandleChatbotOutput(message=response)
