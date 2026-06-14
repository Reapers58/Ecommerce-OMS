from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.coupon_model import Coupon

router = APIRouter()


@router.delete("/{id}")
def delete_coupon(
    id: int,
    db: Session = Depends(get_db)
):
    coupon = (
        db.query(Coupon)
        .filter(Coupon.coupon_id == id)
        .first()
    )

    if coupon:
        db.delete(coupon)
        db.commit()

    return {
        "message": "Coupon deleted successfully"
    }