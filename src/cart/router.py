from fastapi import APIRouter

from src.cart.routers.add_to_cart import router as add_to_cart_router
from src.cart.routers.get_cart import router as get_cart_router
from src.cart.routers.update_cart import router as update_cart_router
from src.cart.routers.remove_from_cart import router as remove_from_cart_router
from src.cart.routers.clear_cart import router as clear_cart_router

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

router.include_router(add_to_cart_router)
router.include_router(get_cart_router)
router.include_router(update_cart_router)
router.include_router(remove_from_cart_router)
router.include_router(clear_cart_router)