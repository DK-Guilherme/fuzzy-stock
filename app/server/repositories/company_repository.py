from server.models.company_model import CompanyModel
from fastapi import Response

company: list[CompanyModel] = [
    {
        "_id": 123,
        "name": "Amazon",
        "CNPJ":  123456789,
        "products": []
    },
    {
        "_id": 321,
        "name": "Google",
        "CNPJ":  1804108341,
        "products": []
    }
]
           
async def find_all_company():
    return company

async def find_company_by_id(id: int):
    print(company)
    for c in company:
        if c['_id'] == id:
            return c
        else: 
            return Response(status_code=404)