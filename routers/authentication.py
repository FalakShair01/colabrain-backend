from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from ..hashPassword import Hash

from fastapi import APIRouter

router = APIRouter(
    tags=['Authentication']
)


def Login(request:schemas.Login ,db: Session = Depends(get_db)):
    user = db.query(models.Company).filter(models.Company.email == request.email)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")
    Hash.verify_password(plain_password=request.password, hashed_password=user.password)

    return 
