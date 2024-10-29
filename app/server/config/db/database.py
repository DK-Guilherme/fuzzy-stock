import psycopg2

def get_database_connection():
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="3693",
        database="fuzzystock"
    )