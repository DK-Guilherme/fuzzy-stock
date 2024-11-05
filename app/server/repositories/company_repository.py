from json import dumps
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
    
async def get_all_company_from_db():
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        query = "select * from company"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()
        return result
    except () as e:
        print(e)
        return e
    
async def get_company_from_db_by_id(id: str):
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        query = f"select * from company where id = {id}"
        cursor.execute(query)
        query_result = cursor.fetchone()
        connection.commit()
        connection.close()
        return query_result
    except () as e:
        print(e)
        return e