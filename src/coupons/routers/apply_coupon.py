from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.coupon_model import Coupon
from src.coupons.schemas.apply_coupon_schema import ApplyCouponSchema

router = APIRouter()


@router.post("/apply-coupon")
def apply_coupon(
    coupon_data: ApplyCouponSchema,
    db: Session = Depends(get_db)
):
    coupon = (
        db.query(Coupon)
        .filter(Coupon.code == coupon_data.coupon_code)
        .first()
    )

    if coupon:
        return {
            "order_id": coupon_data.order_id,
            "coupon_code": coupon.code,
            "discount_percent": coupon.discount_percent
        }

    return {
        "message": "Invalid coupon"
    }