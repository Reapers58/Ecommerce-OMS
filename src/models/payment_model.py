from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base


class Payment(Base):
    __tablename__ = "payments"

    payment_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.order_id")
    )

    payment_method: Mapped[str] = mapped_column(
        String(50)
    )

    transaction_id: Mapped[str] = mapped_column(
        String(255)
    )

    payment_status: Mapped[str] = mapped_column(
        String(50)
    )

    order = relationship(
        "Order",
        back_populates="payment"
    )