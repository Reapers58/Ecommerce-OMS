from fastapi import APIRouter

router = APIRouter()


@router.get("/products/top-selling")
def top_selling_products():
    return []