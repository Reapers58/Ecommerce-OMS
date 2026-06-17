from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import Product

router = APIRouter()


@router.get("/top-selling")
def top_selling_products(
    db: Session = Depends(get_db)
):
    return (
        db.query(Product)
        .order_by(Product.stock.desc())
        .limit(10)
        .all()
    )