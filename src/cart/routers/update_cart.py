from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.cart.schemas.cart_item_schema import CartItemSchema
from src.models.cart_item_model import CartItem

router = APIRouter()


@router.put("/update")
def update_cart(
    item_data: CartItemSchema,
    db: Session = Depends(get_db)
):
    item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == item_data.cart_id,
            CartItem.product_id == item_data.product_id
        )
        .first()
    )

    if item:
        item.quantity = item_data.quantity
        db.commit()
        db.refresh(item)

    return item