from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.category_model import Category
from src.categories.schemas.category_schema import CategorySchema

router = APIRouter()


@router.put("/{id}")
def update_category(
    id: int,
    category_data: CategorySchema,
    db: Session = Depends(get_db)
):
    category = (
        db.query(Category)
        .filter(Category.category_id == id)
        .first()
    )

    if category:
        category.category_name = category_data.category_name
        category.description = category_data.description

        db.commit()
        db.refresh(category)

    return category