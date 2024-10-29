from pydantic import BaseModel
from typing import List
from server.config.db.database import get_database_connection
from server.models.company_model import CompanyModel

async def create_company_repo(company: CompanyModel):
    try: 
        connection = get_database_connection()
        cursor = connection.cursor()
        query = "INSERT INTO company (id, name, cnpj) VALUES (%s, %s, %s)"
        values = (company.id, company.name, company.cnpj)
        cursor.execute(query, values)
        connection.commit()
        connection.close()
    except () as e:
        print(e)
        return e