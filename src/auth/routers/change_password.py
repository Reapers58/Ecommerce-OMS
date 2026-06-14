from fastapi import APIRouter

from src.auth.schemas.change_password_schema import ChangePasswordSchema

router = APIRouter()


@router.put("/change-password")
def change_password(
    password_data: ChangePasswordSchema
):
    return {
        "message": "Password changed successfully"
    }