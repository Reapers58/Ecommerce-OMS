from fastapi import APIRouter

router = APIRouter()


@router.get("/me")
def current_user():
    return {
        "message": "Current user endpoint"
    }