from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from server.services.company_service import (
    create_company,
    get_all_companies,
    get_company_by_id
)
from server.models.company_model import CompanyModel

router = APIRouter()

@router.get("/get_companies", response_description="create company")
async def get_companies():
    try:
        companies_list = await get_all_companies()
        return companies_list
    except () as e:
        print(e)
        return JSONResponse(status_code=500)

@router.post("/", response_description="create company")
async def post_company(company: CompanyModel):
    try:
        await create_company(company)
    except () as e:
        return JSONResponse(status_code=500)
    
@router.get("/get_company/{id}")
async def get_company(id: str):
    try:
        company = await get_company_by_id(id)
        return company
    except () as e:
        print(e)
        return e