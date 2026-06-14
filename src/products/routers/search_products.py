from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import Product

router = APIRouter()


@router.get("/search")
def search_products(
    name: str,
    db: Session = Depends(get_db)
):
    return (
        db.query(Product)
        .filter(Product.product_name.ilike(f"%{name}%"))
        .all()
    )