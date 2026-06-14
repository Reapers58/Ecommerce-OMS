from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.review_model import Review
from src.reviews.schemas.review_schema import ReviewSchema

router = APIRouter()


@router.put("/{id}")
def update_review(
    id: int,
    review_data: ReviewSchema,
    db: Session = Depends(get_db)
):
    review = (
        db.query(Review)
        .filter(Review.review_id == id)
        .first()
    )

    if review:
        review.user_id = review_data.user_id
        review.product_id = review_data.product_id
        review.rating = review_data.rating
        review.comment = review_data.comment

        db.commit()
        db.refresh(review)

    return review