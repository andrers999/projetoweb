import psycopg2

def conectardb():
    con = psycopg2.connect(
        host='localhost',
        database='postgr',
        user='postgres',
        password='12345'
    )
    return con

