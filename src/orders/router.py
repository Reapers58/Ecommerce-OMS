from fastapi import APIRouter

from src.orders.routers.create_order import router as create_order_router
from src.orders.routers.get_orders import router as get_orders_router

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

router.include_router(create_order_router)
router.include_router(get_orders_router)