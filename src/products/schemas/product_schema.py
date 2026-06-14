from pydantic import BaseModel


class ProductSchema(BaseModel):
    seller_id: int
    category_id: int
    product_name: str
    description: str
    price: float
    stock: int
    brand: str
    status: str


class ProductResponseSchema(ProductSchema):
    product_id: int

    class Config:
        from_attributes = True