from fastapi import APIRouter

from src.product_images.routers.upload_image import router as upload_image_router
from src.product_images.routers.get_product_images import router as get_product_images_router

router = APIRouter(
    prefix="/products",
    tags=["Product Images"]
)

router.include_router(upload_image_router)
router.include_router(get_product_images_router)