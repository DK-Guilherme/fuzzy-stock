from fastapi import Response
from bson.json_util import dumps
import json

from server.repositories.company_repository import (
    find_all_company,
    find_company_by_id,
    get_companies_products,
    post_company
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

async def create_company(dict):
    post_company(dict)
    return Response(status_code=203)