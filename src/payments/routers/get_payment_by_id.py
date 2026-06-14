from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.payment_model import Payment

router = APIRouter()


@router.get("/{id}")
def get_payment_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Payment)
        .filter(Payment.payment_id == id)
        .first()
    )