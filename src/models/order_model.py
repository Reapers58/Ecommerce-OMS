from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    total_amount: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    order_status: Mapped[str] = mapped_column(
        String(50)
    )

    shipping_address: Mapped[str] = mapped_column(
        Text
    )

    order_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=True
    )

    user = relationship(
        "User",
        back_populates="orders"
    )

    items = relationship(
        "OrderItem",
        back_populates="order"
    )

    payment = relationship(
        "Payment",
        back_populates="order"
    )

