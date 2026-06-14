from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.user_model import User
from src.models.product_model import Product
from src.models.order_model import Order

router = APIRouter()


@router.get("/admin")
def admin_dashboard(
    db: Session = Depends(get_db)
):
    return {
        "total_users": db.query(User).count(),
        "total_products": db.query(Product).count(),
        "total_orders": db.query(Order).count(),
        "pending_orders": db.query(Order)
                            .filter(Order.order_status == "Pending")
                            .count(),
        "total_sales": 0
    }