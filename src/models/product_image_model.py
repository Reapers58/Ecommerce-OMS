from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base


class ProductImage(Base):
    __tablename__ = "product_images"

    image_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.product_id")
    )

    image_url: Mapped[str] = mapped_column(
        String(255)
    )

    product = relationship(
        "Product",
        back_populates="images"
    )
    