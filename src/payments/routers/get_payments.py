from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.payment_model import Payment

router = APIRouter()


@router.get("/")
def get_payments(
    db: Session = Depends(get_db)
):
    return db.query(Payment).all()