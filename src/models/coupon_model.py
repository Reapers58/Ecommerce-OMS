from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Coupon(Base):
    __tablename__ = "coupons"

    coupon_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    code: Mapped[str] = mapped_column(
        String(100)
    )

    discount_percent: Mapped[int] = mapped_column(
        Integer
    )

    active: Mapped[bool] = mapped_column(
        Boolean
    )