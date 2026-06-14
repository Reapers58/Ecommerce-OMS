from fastapi import APIRouter

from src.products.routers.create_product import router as create_product_router
from src.products.routers.get_products import router as get_products_router
from src.products.routers.get_product_by_id import router as get_product_by_id_router
from src.products.routers.update_product import router as update_product_router
from src.products.routers.delete_product import router as delete_product_router
from src.products.routers.search_products import router as search_products_router

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

router.include_router(create_product_router)
router.include_router(get_products_router)
router.include_router(get_product_by_id_router)
router.include_router(update_product_router)
router.include_router(delete_product_router)
router.include_router(search_products_router)