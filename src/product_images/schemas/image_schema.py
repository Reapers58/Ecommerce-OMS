from pydantic import BaseModel


class ProductImageSchema(BaseModel):
    product_id: int
    image_url: str