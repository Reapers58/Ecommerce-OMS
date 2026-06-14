from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.order_model import Order
from src.orders.schemas.order_schema import OrderSchema

router = APIRouter()


@router.post("/create")
def create_order(
    order_data: OrderSchema,
    db: Session = Depends(get_db)
):
    order = Order(
        user_id=order_data.user_id,
        total_amount=order_data.total_amount,
        order_status=order_data.order_status,
        shipping_address=order_data.shipping_address
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order