from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.order_model import Order

router = APIRouter()


@router.get("/orders/recent")
def recent_orders(
    db: Session = Depends(get_db)
):
    return (
        db.query(Order)
        .limit(10)
        .all()
    )