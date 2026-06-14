from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.review_model import Review

router = APIRouter()


@router.get("/")
def get_reviews(
    db: Session = Depends(get_db)
):
    return db.query(Review).all()