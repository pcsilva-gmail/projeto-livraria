import psycopg2
import psycopg2.pool

from settings import (
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

class ConexaoFactory:
    
    def get_conexao(self):
        return psycopg2.pool.SimpleConnectionPool(1, 6, host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD ).getconn()