from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.categories.schemas.category_schema import CategorySchema
from src.database import get_db
from src.models.category_model import Category

router = APIRouter()


@router.post("/")
def create_category(
    category_data: CategorySchema,
    db: Session = Depends(get_db)
):
    category = Category(
        category_name=category_data.category_name,
        description=category_data.description
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category