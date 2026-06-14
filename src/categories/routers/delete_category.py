from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.category_model import Category

router = APIRouter()


@router.delete("/{id}")
def delete_category(
    id: int,
    db: Session = Depends(get_db)
):
    category = (
        db.query(Category)
        .filter(Category.category_id == id)
        .first()
    )

    if category:
        db.delete(category)
        db.commit()

    return {
        "message": "Category deleted successfully"
    }