from pydantic import BaseModel


class PaymentSchema(BaseModel):
    order_id: int
    payment_method: str
    transaction_id: str
    payment_status: str