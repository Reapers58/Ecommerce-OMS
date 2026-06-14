from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class Wishlist(Base):
    __tablename__ = "wishlist"

    wishlist_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.product_id")
    )

    user = relationship(
        "User",
        back_populates="wishlist_items"
    )

    product = relationship(
        "Product",
        back_populates="wishlist_items"
    )