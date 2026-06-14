from fastapi import APIRouter

from src.auth.router import router as auth_router
from src.categories.router import router as categories_router
from src.products.router import router as products_router
from src.cart.router import router as cart_router
from src.orders.router import router as orders_router
from src.payments.router import router as payments_router
from src.wishlist.router import router as wishlist_router
from src.reviews.router import router as reviews_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(categories_router)
router.include_router(products_router)
router.include_router(cart_router)
router.include_router(orders_router)
router.include_router(payments_router)
router.include_router(wishlist_router)
router.include_router(reviews_router)

