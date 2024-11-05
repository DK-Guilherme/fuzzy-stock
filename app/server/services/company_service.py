from server.repositories.company_repository import (
    get_all_company_from_db,
    create_company_repo,
    get_company_from_db_by_id
)
from server.models.company_model import CompanyModel

async def create_company(company: CompanyModel):
    try:
        await create_company_repo(company)
    except () as e:
        print(e)
        
async def get_all_companies() -> list[CompanyModel]:
    try:
        obj_list: list[CompanyModel] = []
        companies_list = await get_all_company_from_db()
        for companie in companies_list:
            companie_obj = CompanyModel(id=companie[0], name=companie[1], cnpj=companie[2])
            obj_list.append(companie_obj)
        print(obj_list)
        return obj_list
    except () as e:
        print(e)
        
async def get_company_by_id(id: str) -> CompanyModel:
    try:
        company = await get_company_from_db_by_id(id)
        print(company)
        company_obj: CompanyModel = CompanyModel(id=company[0], name=company[1], cnpj=company[2])
        return company_obj
    except () as e:
        print(e)
        return e