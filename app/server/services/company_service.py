from bson.json_util import dumps
import json

from server.repositories.company_repository import (
    find_all_company
)

async def find_all():
    res = await find_all_company()
    return res