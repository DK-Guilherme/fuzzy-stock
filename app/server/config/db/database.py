import psycopg2
import os
from dotenv import load_dotenv

load_dotenv('./env')
host = os.environ.get("HOST")
user = os.environ.get("USER")
password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")

def get_database_connection():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )