from datetime import datetime
import uuid
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID

class Message(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4, alias="_id")
    msg: str
    timestamp: str

    class Config:
        json_encoders = {UUID: str}

class Chat(BaseModel):
    token: str
    messages: List[Message]
    name: str
    session_start: str

    class Config:
        json_encoders = {UUID: str}

    @classmethod
    def generate_timestamp(cls) -> str:
        return str(datetime.now())

    def __init__(self, **data):
        timestamp = data.get("timestamp") or self.generate_timestamp()
        session_start = data.get("session_start") or self.generate_timestamp()
        super().__init__(**data, timestamp=timestamp, session_start=session_start)
