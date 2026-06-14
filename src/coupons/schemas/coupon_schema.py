from pydantic import BaseModel


class CouponSchema(BaseModel):
    code: str
    discount_percent: int
    active: bool = True