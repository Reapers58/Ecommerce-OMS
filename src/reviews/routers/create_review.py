from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.review_model import Review
from src.reviews.schemas.review_schema import ReviewSchema

router = APIRouter()


@router.post("/")
def create_review(
    review_data: ReviewSchema,
    db: Session = Depends(get_db)
):
    review = Review(
        user_id=review_data.user_id,
        product_id=review_data.product_id,
        rating=review_data.rating,
        comment=review_data.comment
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review