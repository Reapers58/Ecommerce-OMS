from pydantic import BaseModel


class CategorySchema(BaseModel):
    category_name: str
    description: str | None = None


class CategoryResponseSchema(CategorySchema):
    category_id: int

    class Config:
        from_attributes = True