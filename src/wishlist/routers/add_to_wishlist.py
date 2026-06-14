from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.wishlist_model import Wishlist
from src.wishlist.schemas.wishlist_schema import WishlistSchema

router = APIRouter()


@router.post("/add")
def add_to_wishlist(
    wishlist_data: WishlistSchema,
    db: Session = Depends(get_db)
):
    wishlist_item = Wishlist(
        user_id=wishlist_data.user_id,
        product_id=wishlist_data.product_id
    )

    db.add(wishlist_item)
    db.commit()
    db.refresh(wishlist_item)

    return wishlist_item