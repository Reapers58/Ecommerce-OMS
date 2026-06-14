from fastapi import APIRouter

from src.wishlist.routers.add_to_wishlist import router as add_to_wishlist_router
from src.wishlist.routers.get_wishlist import router as get_wishlist_router

router = APIRouter(
    prefix="/wishlist",
    tags=["Wishlist"]
)

router.include_router(add_to_wishlist_router)
router.include_router(get_wishlist_router)