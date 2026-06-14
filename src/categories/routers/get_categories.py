from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.category_model import Category

router = APIRouter()


@router.get("/")
def get_categories(
    db: Session = Depends(get_db)
):
    return db.query(Category).all()