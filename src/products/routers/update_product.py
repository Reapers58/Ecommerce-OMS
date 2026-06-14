from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.product_model import Product
from src.products.schemas.product_schema import ProductSchema

router = APIRouter()


@router.put("/{id}")
def update_product(
    id: int,
    product_data: ProductSchema,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.product_id == id)
        .first()
    )

    if product:
        product.seller_id = product_data.seller_id
        product.category_id = product_data.category_id
        product.product_name = product_data.product_name
        product.description = product_data.description
        product.price = product_data.price
        product.stock = product_data.stock
        product.brand = product_data.brand
        product.status = product_data.status

        db.commit()
        db.refresh(product)

    return product