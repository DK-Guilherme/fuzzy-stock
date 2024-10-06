from bson.json_util import dumps
import json

from server.repositories.company_repository import (
    find_all_company,
    find_company_by_id,
    get_companies_products
)

async def find_all():
    res = await find_all_company()
    return res

async def find_by_id(id: int):
    res = await find_company_by_id(id)
    return res

async def find_company_products(id: int):
    res = await get_companies_products(id)
    print(res)
    return res