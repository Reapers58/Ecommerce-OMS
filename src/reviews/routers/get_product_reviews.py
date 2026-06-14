from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.review_model import Review

router = APIRouter()


@router.get("/products/{id}/reviews")
def get_product_reviews(
    id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Review)
        .filter(Review.product_id == id)
        .all()
    )