from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.order_model import Order
from src.orders.schemas.order_status_schema import OrderStatusSchema

router = APIRouter()


@router.put("/{id}/status")
def update_order_status(
    id: int,
    status_data: OrderStatusSchema,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.order_id == id)
        .first()
    )

    if order:
        order.order_status = status_data.status
        db.commit()
        db.refresh(order)

    return order