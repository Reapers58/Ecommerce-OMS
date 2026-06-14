from fastapi import APIRouter

router = APIRouter()


@router.get("/customer")
def customer_dashboard():
    return {
        "orders": 0,
        "wishlist_items": 0,
        "cart_items": 0
    }