from fastapi import APIRouter

from server.services.company_service import (
    find_all,
    find_by_id
)

router = APIRouter()

@router.get("/", response_description="Companies found")
async def find_all_companies():
    res = await find_all()
    return res

@router.get("/{id}", response_description="Company found!")
async def find_company_by_id(id: int):
    res = await find_by_id(id)
    return res