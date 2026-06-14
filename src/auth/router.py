from fastapi import APIRouter

from src.auth.schemas.login_schema import LoginSchema
from src.auth.schemas.user_schema import UserSchema

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/login",
    response_model=UserSchema
)
def login(login_data: LoginSchema):
    return {
        "user_id": 1
    }