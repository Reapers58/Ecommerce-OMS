from pydantic import BaseModel


class ApplyCouponSchema(BaseModel):
    order_id: int
    coupon_code: str