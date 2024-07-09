from fastapi import APIRouter, Request

from openaoe.backend.model.deepseek import DeepSeekChatCompletionBody
from openaoe.backend.service.service_deepseek import chat_stream

router = APIRouter()


@router.post("/v1/text/chat-stream", tags=["DeepSeek"])
async def deepseek_chat_stream(request: Request, body: DeepSeekChatCompletionBody):
    """
    chat stream api for DeepSeek
    @param request: fastapi request
    @param body: request body
    @return: response
    """
    ret = chat_stream(request, body)
    return ret
