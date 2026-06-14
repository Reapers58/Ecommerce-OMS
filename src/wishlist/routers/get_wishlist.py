from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.wishlist_model import Wishlist

router = APIRouter()


@router.get("/")
def get_wishlist(
    db: Session = Depends(get_db)
):
    return db.query(Wishlist).all()