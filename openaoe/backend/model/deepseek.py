from typing import Optional, List, Union

from pydantic import BaseModel


class Context(BaseModel):
    send_type: str = 'assistant'
    sender_type: str = "assistant"
    text: str = ''


class RoleMeta(BaseModel):
    user_name: Optional[str] = 'user'
    bot_name: Optional[str] = 'assistant'


class Messages(BaseModel):
    sender_type: str
    text: str


class DeepSeekChatCompletionBody(BaseModel):
    model: Optional[str] = 'deepseek-chat'
    prompt: str
    temperature: Optional[float] = 1
    messages: Optional[List[Context]] = None
    role_meta: Optional[RoleMeta] = None
    type: Optional[str] = 'text'
    timeout: Optional[int] = 600
