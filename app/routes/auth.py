from fastapi import APIRouter, HTTPException, status, Depends
from app import oauth2
from .. import database, models, schemas, utils
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/login")
def login(
    credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = (
        db.query(models.User).filter(models.User.email == credentials.username).first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password is incorrect",
        )
    is_password_correct = utils.verify_password(credentials.password, user.password)
    if not is_password_correct:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password is incorrect",
        )
    access_token = oauth2.create_access_token({"user_id": user.id})
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
