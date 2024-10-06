from fastapi import APIRouter

from server.services.company_service import (
    find_all
)

router = APIRouter()

@router.get("/", response_description="Companies found")
async def find_all_companies():
    res = await find_all()
    return res