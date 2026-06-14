from pydantic import BaseModel


class OrderSchema(BaseModel):
    user_id: int
    total_amount: float
    order_status: str
    shipping_address: str