from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.coupon_model import Coupon
from src.coupons.schemas.coupon_schema import CouponSchema

router = APIRouter()


@router.post("/")
def create_coupon(
    coupon_data: CouponSchema,
    db: Session = Depends(get_db)
):
    coupon = Coupon(
        code=coupon_data.code,
        discount_percent=coupon_data.discount_percent,
        active=coupon_data.active
    )

    db.add(coupon)
    db.commit()
    db.refresh(coupon)

    return coupon