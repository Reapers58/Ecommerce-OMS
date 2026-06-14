from sqlalchemy import ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    seller_id: Mapped[int] = mapped_column(
        ForeignKey("sellers.seller_id")
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.category_id")
    )

    product_name: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    price: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    stock: Mapped[int] = mapped_column(
        Integer
    )

    brand: Mapped[str] = mapped_column(
        String(100)
    )

    status: Mapped[str] = mapped_column(
        String(50)
    )

    seller = relationship(
        "Seller",
        back_populates="products"
    )

    images = relationship(
        "ProductImage",
        back_populates="product"
    )

    category = relationship(
        "Category",
        back_populates="products"
    )

    reviews = relationship(
        "Review",
        back_populates="product"
    )

    wishlist_items = relationship(
        "Wishlist",
        back_populates="product"
    )