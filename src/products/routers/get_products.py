from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import Product

router = APIRouter()


@router.get("/")
def get_products(
    category: int | None = None,
    brand: str | None = None,
    sort: str | None = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    if category:
        query = query.filter(Product.category_id == category)

    if brand:
        query = query.filter(Product.brand == brand)

    if sort == "price":
        query = query.order_by(Product.price)

    offset = (page - 1) * limit

    return (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )