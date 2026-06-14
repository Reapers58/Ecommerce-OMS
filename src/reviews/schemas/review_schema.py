from pydantic import BaseModel


class ReviewSchema(BaseModel):
    user_id: int
    product_id: int
    rating: int
    comment: str