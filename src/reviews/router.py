from fastapi import APIRouter

from src.reviews.routers.create_review import router as create_review_router
from src.reviews.routers.get_reviews import router as get_reviews_router

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

router.include_router(create_review_router)
router.include_router(get_reviews_router)