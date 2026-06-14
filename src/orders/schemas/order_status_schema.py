from pydantic import BaseModel


class OrderStatusSchema(BaseModel):
    status: str