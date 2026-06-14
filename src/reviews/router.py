from fastapi import APIRouter

from src.reviews.routers.create_review import router as create_review_router
from src.reviews.routers.get_reviews import router as get_reviews_router
from src.reviews.routers.get_product_reviews import router as get_product_reviews_router
from src.reviews.routers.update_review import router as update_review_router
from src.reviews.routers.delete_review import router as delete_review_router

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

router.include_router(create_review_router)
router.include_router(get_reviews_router)
router.include_router(get_product_reviews_router)
router.include_router(update_review_router)
router.include_router(delete_review_router)