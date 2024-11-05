from dotenv import load_dotenv
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from server.services.company_service import (
    # find_all,
    # find_by_id,
    # find_company_products,
    create_company
)
from server.models.company_model import CompanyModel
import sqlalchemy

router = APIRouter()

# @router.get("/", response_description="Companies found")
# async def find_all_companies():
#     res = await find_all()
#     return res

# @router.get("/{id}", response_description="Company found!")
# async def find_company_by_id(id: int):
#     res = await find_by_id(id)
#     return res 

# @router.get("/{id}/products", response_description="company products")
# async def get_companies_products(id: int):
#     res = await find_company_products(id)
#     if res:
#         return res
#     else:
#         return Response(status_code=404)
    
@router.post("/", response_description="VAI TOMA NO CU")
async def post_company(company: CompanyModel):
    try:
        await create_company(company)
    except () as e:
        return JSONResponse(status_code=500)