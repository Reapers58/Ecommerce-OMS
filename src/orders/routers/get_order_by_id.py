from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.order_model import Order

router = APIRouter()


@router.get("/{id}")
def get_order_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Order)
        .filter(Order.order_id == id)
        .first()
    )