from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    item_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    cart_id: Mapped[int] = mapped_column(
        ForeignKey("cart.cart_id")
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.product_id")
    )

    quantity: Mapped[int] = mapped_column(
        Integer
    )

    cart = relationship(
        "Cart",
        back_populates="items"
    )

    product = relationship(
        "Product"
    )