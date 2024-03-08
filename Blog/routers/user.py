from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def users(request:schemas.User, db: Session=Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',response_model=schemas.ShowUser,status_code=status.HTTP_200_OK)
def get_user(id:int,db:Session=Depends(get_db)):
    return user.get(id, db)