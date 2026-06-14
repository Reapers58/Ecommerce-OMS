from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.category_model import Category

router = APIRouter()


@router.get("/{id}")
def get_category_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Category)
        .filter(Category.category_id == id)
        .first()
    )