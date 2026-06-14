from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.cart_item_model import CartItem

router = APIRouter()


@router.get("/")
def get_cart(
    db: Session = Depends(get_db)
):
    return db.query(CartItem).all()