from fastapi import APIRouter

from src.orders.routers.create_order import router as create_order_router
from src.orders.routers.get_orders import router as get_orders_router
from src.orders.routers.get_order_by_id import router as get_order_by_id_router
from src.orders.routers.update_order_status import router as update_order_status_router
from src.orders.routers.delete_order import router as delete_order_router

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

router.include_router(create_order_router)
router.include_router(get_orders_router)
router.include_router(get_order_by_id_router)
router.include_router(update_order_status_router)
router.include_router(delete_order_router)