from pydantic import BaseModel


class GeckoPingOutput(BaseModel):
    gecko_says: str