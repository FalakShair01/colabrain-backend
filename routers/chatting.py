from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import models, schemas



router = APIRouter(
    prefix="/chat",
    tags=['Chatting']
)


# @router.post('/', response_model=List[schemas.showChat])
# async def create_new(request: schemas.creatNewConversation, db:Session=Depends(get_db)):
#     conversation = models.Conversation(chat_id=1,req=request.req, res=request.res)
#     return conversation
