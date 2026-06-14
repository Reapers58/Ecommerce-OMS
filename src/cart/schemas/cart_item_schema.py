from pydantic import BaseModel


class CartItemSchema(BaseModel):
    cart_id: int
    product_id: int
    quantity: int