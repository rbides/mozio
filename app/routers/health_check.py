from fastapi import APIRouter


router = APIRouter(
    prefix="/health",
)

@router.get("", status_code=200)
def health_check():
    """Check service availability"""
    return {"Service status: OK"}
