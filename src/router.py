from fastapi import APIRouter

from src.auth.router import router as auth_router
from src.categories.router import router as categories_router
from src.categories.routers.get_category_by_id import router as get_category_by_id_router
from src.categories.routers.update_category import router as update_category_router
from src.categories.routers.delete_category import router as delete_category_router
from src.products.router import router as products_router
from src.product_images.router import router as product_images_router 
from src.cart.router import router as cart_router
from src.orders.router import router as orders_router
from src.payments.router import router as payments_router
from src.wishlist.router import router as wishlist_router
from src.reviews.router import router as reviews_router
from src.auth.routers.profile import router as profile_router
from src.auth.routers.change_password import router as change_password_router
from src.coupons.router import router as coupons_router
from src.dashboard.router import router as dashboard_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(categories_router)
router.include_router(products_router)
router.include_router(cart_router)
router.include_router(orders_router)
router.include_router(payments_router)
router.include_router(wishlist_router)
router.include_router(reviews_router)
router.include_router(profile_router)
router.include_router(change_password_router)
router.include_router(get_category_by_id_router)
router.include_router(update_category_router)
router.include_router(delete_category_router)
router.include_router(product_images_router)
router.include_router(coupons_router)
router.include_router(dashboard_router)