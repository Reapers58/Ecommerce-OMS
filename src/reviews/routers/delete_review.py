from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.review_model import Review

router = APIRouter()


@router.delete("/{id}")
def delete_review(
    id: int,
    db: Session = Depends(get_db)
):
    review = (
        db.query(Review)
        .filter(Review.review_id == id)
        .first()
    )

    if review:
        db.delete(review)
        db.commit()

    return {
        "message": "Review deleted successfully"
    }