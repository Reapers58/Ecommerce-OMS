from fastapi import APIRouter

from src.coupons.routers.create_coupon import router as create_coupon_router
from src.coupons.routers.get_coupons import router as get_coupons_router
from src.coupons.routers.update_coupon import router as update_coupon_router
from src.coupons.routers.delete_coupon import router as delete_coupon_router
from src.coupons.routers.apply_coupon import router as apply_coupon_router

router = APIRouter(
    prefix="/coupons",
    tags=["Coupons"]
)

router.include_router(create_coupon_router)
router.include_router(get_coupons_router)
router.include_router(update_coupon_router)
router.include_router(delete_coupon_router)
router.include_router(apply_coupon_router)