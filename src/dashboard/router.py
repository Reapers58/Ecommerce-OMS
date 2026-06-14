from fastapi import APIRouter

from src.dashboard.routers.admin_dashboard import router as admin_dashboard_router
from src.dashboard.routers.seller_dashboard import router as seller_dashboard_router
from src.dashboard.routers.customer_dashboard import router as customer_dashboard_router
from src.dashboard.routers.low_stock_products import router as low_stock_products_router
from src.dashboard.routers.top_selling_products import router as top_selling_products_router
from src.dashboard.routers.recent_orders import router as recent_orders_router

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

router.include_router(admin_dashboard_router)
router.include_router(seller_dashboard_router)
router.include_router(customer_dashboard_router)
router.include_router(low_stock_products_router)
router.include_router(top_selling_products_router)
router.include_router(recent_orders_router)