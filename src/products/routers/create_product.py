from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import Product
from src.products.schemas.product_schema import ProductSchema

router = APIRouter()


@router.post("/")
def create_product(
    product_data: ProductSchema,
    db: Session = Depends(get_db)
):
    product = Product(
        seller_id=product_data.seller_id,
        category_id=product_data.category_id,
        product_name=product_data.product_name,
        description=product_data.description,
        price=product_data.price,
        stock=product_data.stock,
        brand=product_data.brand,
        status=product_data.status
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product