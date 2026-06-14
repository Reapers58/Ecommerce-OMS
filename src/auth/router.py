from fastapi import APIRouter

from src.auth.routers.login import router as login_router
from src.auth.routers.signup import router as signup_router
from src.auth.routers.current_user import router as current_user_router

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(signup_router)
router.include_router(login_router)
router.include_router(current_user_router)