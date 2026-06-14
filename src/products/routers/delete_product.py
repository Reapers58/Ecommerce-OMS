from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import Product

router = APIRouter()


@router.delete("/{id}")
def delete_product(
    id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.product_id == id)
        .first()
    )

    if product:
        db.delete(product)
        db.commit()

    return {
        "message": "Product deleted successfully"
    }