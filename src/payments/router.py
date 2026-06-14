from fastapi import APIRouter

from src.payments.routers.create_payment import router as create_payment_router
from src.payments.routers.get_payments import router as get_payments_router

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

router.include_router(create_payment_router)
router.include_router(get_payments_router)