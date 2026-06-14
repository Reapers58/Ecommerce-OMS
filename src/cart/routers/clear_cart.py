from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.cart_item_model import CartItem

router = APIRouter()


@router.delete("/clear")
def clear_cart(
    db: Session = Depends(get_db)
):
    db.query(CartItem).delete()
    db.commit()

    return {
        "message": "Cart cleared successfully"
    }