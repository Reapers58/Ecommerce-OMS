from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.coupon_model import Coupon
from src.coupons.schemas.coupon_schema import CouponSchema

router = APIRouter()


@router.put("/{id}")
def update_coupon(
    id: int,
    coupon_data: CouponSchema,
    db: Session = Depends(get_db)
):
    coupon = (
        db.query(Coupon)
        .filter(Coupon.coupon_id == id)
        .first()
    )

    if coupon:
        coupon.code = coupon_data.code
        coupon.discount_percent = coupon_data.discount_percent
        coupon.active = coupon_data.active

        db.commit()
        db.refresh(coupon)

    return coupon