from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.cart_item_model import CartItem
from src.cart.schemas.cart_item_schema import CartItemSchema

router = APIRouter()


@router.post("/add")
def add_to_cart(
    item_data: CartItemSchema,
    db: Session = Depends(get_db)
):
    item = CartItem(
        cart_id=item_data.cart_id,
        product_id=item_data.product_id,
        quantity=item_data.quantity
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item