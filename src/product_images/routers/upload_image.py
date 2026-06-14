from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_image_model import ProductImage
from src.product_images.schemas.image_schema import ProductImageSchema

router = APIRouter()


@router.post("/upload-image")
def upload_image(
    image_data: ProductImageSchema,
    db: Session = Depends(get_db)
):
    image = ProductImage(
        product_id=image_data.product_id,
        image_url=image_data.image_url
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    return image