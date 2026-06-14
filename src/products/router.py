from fastapi import APIRouter

from src.products.routers.create_product import router as create_product_router
from src.products.routers.get_products import router as get_products_router

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

router.include_router(create_product_router)
router.include_router(get_products_router)