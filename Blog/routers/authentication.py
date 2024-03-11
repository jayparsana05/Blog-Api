from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, token
from ..hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(request.username == models.User.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='User not found')
    
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect Password')
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}