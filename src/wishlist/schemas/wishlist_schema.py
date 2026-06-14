from pydantic import BaseModel


class WishlistSchema(BaseModel):
    user_id: int
    product_id: int