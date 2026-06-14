from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.auth.controllers.get_user_by_email import get_user_by_email
from src.auth.controllers.hash_password import hash_password
from src.auth.schemas.register_schema import RegisterSchema
from src.database import get_db
from src.models.user_model import User

router = APIRouter()


@router.post("/signup")
def signup(
    user_data: RegisterSchema,
    db: Session = Depends(get_db)
):
    existing_user = get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password=hash_password(
            user_data.password
        ),
        role=user_data.role,
        mobile=user_data.mobile
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }