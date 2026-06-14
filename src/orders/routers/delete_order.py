from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.order_model import Order

router = APIRouter()


@router.delete("/{id}")
def delete_order(
    id: int,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.order_id == id)
        .first()
    )

    if order:
        db.delete(order)
        db.commit()

    return {
        "message": "Order cancelled successfully"
    }