from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.coupon_model import Coupon

router = APIRouter()


@router.get("/")
def get_coupons(
    db: Session = Depends(get_db)
):
    return db.query(Coupon).all()