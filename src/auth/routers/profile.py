from fastapi import APIRouter

router = APIRouter()


@router.get("/profile")
def profile():
    return {
        "id": 1,
        "name": "Rahul Sharma",
        "email": "rahul@gmail.com",
        "role": "customer"
    }