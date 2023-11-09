from pydantic import BaseModel

class Message(BaseModel):
    content: str

class Thread(BaseModel):
    messages: list[Message] = []
