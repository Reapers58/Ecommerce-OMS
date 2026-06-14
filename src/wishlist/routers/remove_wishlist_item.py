from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.wishlist_model import Wishlist

router = APIRouter()


@router.delete("/{id}")
def remove_wishlist_item(
    id: int,
    db: Session = Depends(get_db)
):
    item = (
        db.query(Wishlist)
        .filter(Wishlist.wishlist_id == id)
        .first()
    )

    if item:
        db.delete(item)
        db.commit()

    return {
        "message": "Wishlist item removed successfully"
    }