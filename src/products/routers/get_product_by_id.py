from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import Product

router = APIRouter()


@router.get("/{id}")
def get_product_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Product)
        .filter(Product.product_id == id)
        .first()
    )