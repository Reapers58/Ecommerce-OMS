from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.cart_item_model import CartItem

router = APIRouter()


@router.delete("/remove/{id}")
def remove_from_cart(
    id: int,
    db: Session = Depends(get_db)
):
    item = (
        db.query(CartItem)
        .filter(CartItem.item_id == id)
        .first()
    )

    if item:
        db.delete(item)
        db.commit()

    return {
        "message": "Item removed successfully"
    }