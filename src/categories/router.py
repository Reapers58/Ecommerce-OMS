from fastapi import APIRouter

from src.categories.routers.create_category import router as create_category_router
from src.categories.routers.get_categories import router as get_categories_router

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

router.include_router(create_category_router)
router.include_router(get_categories_router)