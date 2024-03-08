from pydantic import BaseModel


class HandleChatbotInput(BaseModel):
    message: str


class HandleChatbotOutput(BaseModel):
    message: str
    