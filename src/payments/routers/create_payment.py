from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.payment_model import Payment
from src.payments.schemas.payment_schema import PaymentSchema

router = APIRouter()


@router.post("/")
def create_payment(
    payment_data: PaymentSchema,
    db: Session = Depends(get_db)
):
    payment = Payment(
        order_id=payment_data.order_id,
        payment_method=payment_data.payment_method,
        transaction_id=payment_data.transaction_id,
        payment_status=payment_data.payment_status
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    return payment