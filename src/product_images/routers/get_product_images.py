from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_image_model import ProductImage

router = APIRouter()


@router.get("/{id}/images")
def get_product_images(
    id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(ProductImage)
        .filter(ProductImage.product_id == id)
        .all()
    )