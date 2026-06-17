from fastapi import APIRouter

from src.categories.routers.create_category import router as create_category_router
from src.categories.routers.get_categories import router as get_categories_router
from src.categories.routers.get_category_by_id import router as get_category_by_id_router
from src.categories.routers.update_category import router as update_category_router
from src.categories.routers.delete_category import router as delete_category_router

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

router.include_router(create_category_router)
router.include_router(get_categories_router)
router.include_router(get_category_by_id_router)
router.include_router(update_category_router)
router.include_router(delete_category_router)