from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.auth.controllers.authenticate_user import authenticate_user
from src.auth.controllers.create_access_token import create_jwt_token
from src.auth.schemas.login_schema import LoginSchema
from src.auth.schemas.token_schema import TokenSchema
from src.database import get_db

router = APIRouter()


@router.post(
    "/login",
    response_model=TokenSchema
)
def login(
    login_data: LoginSchema,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        login_data.email,
        login_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_jwt_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }