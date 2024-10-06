from fastapi import APIRouter, Response

import server.repositories.company_repository
from server.services.company_service import (
    find_all,
    find_by_id,
    find_company_products
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

@router.get("/{id}/products", response_description="company products")
async def get_companies_products(id: int):
    res = await find_company_products(id)
    if res:
        return res
    else:
        return Response(status_code=404)