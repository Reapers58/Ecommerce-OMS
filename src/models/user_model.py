from sqlalchemy import DateTime,Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(50))
    mobile: Mapped[str] = mapped_column(String(20))

    created_at: Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.utcnow,
    nullable=True
    )
    
    seller = relationship(
        "Seller", 
        back_populates="user"
    )

    cart = relationship(
        "Cart",
        back_populates="user"
    )

    orders = relationship(
        "Order",
        back_populates="user"
    )

    reviews = relationship(
        "Review",
        back_populates="user"
    )

    wishlist_items = relationship(
        "Wishlist",
        back_populates="user"
    )