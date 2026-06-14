from fastapi import APIRouter

from src.cart.routers.add_to_cart import router as add_to_cart_router
from src.cart.routers.get_cart import router as get_cart_router

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

router.include_router(add_to_cart_router)
router.include_router(get_cart_router)