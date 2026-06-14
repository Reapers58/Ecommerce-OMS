from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base


class Seller(Base):
    __tablename__ = "sellers"

    seller_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    company_name: Mapped[str] = mapped_column(
        String(255)
    )

    gst_no: Mapped[str] = mapped_column(
        String(100)
    )

    address: Mapped[str] = mapped_column(
        Text
    )

    user = relationship(
        "User",
        back_populates="seller"
    )

    products = relationship(
        "Product",
        back_populates="seller"
    )