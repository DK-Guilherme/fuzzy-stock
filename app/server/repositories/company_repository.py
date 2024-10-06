from server.models.company_model import CompanyModel
from fastapi import Response

company: list[CompanyModel] = [
    {
        "_id": 123,
        "name": "Amazon",
        "CNPJ":  123456789,
        "products": [{ "produto": "produto"}, { "produto": "produto"}]
    },
    {
        "_id": 321,
        "name": "Google",
        "CNPJ":  1804108341,
        "products": [{ "produto": "produto"}, { "produto": "produto"}]
    }
]
           
async def find_all_company():
    return company

async def find_company_by_id(id: int):
    print(company)
    for c in company:
        if c['_id'] == id:
            return c

async def get_companies_products(id: int):
    for c in company:
        print(c)
        if c['_id'] == id:
            return c['products']
