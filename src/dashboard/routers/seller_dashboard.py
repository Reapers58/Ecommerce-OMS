from fastapi import APIRouter

router = APIRouter()


@router.get("/seller")
def seller_dashboard():
    return {
        "my_products": 0,
        "orders_received": 0,
        "revenue": 0
    }