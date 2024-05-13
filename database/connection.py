import psycopg2

def connect_to_database():
    # Conexão com o banco de dados PostgreSQL
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    # Criação de um cursor para executar consultas SQL
    cursor = conn.cursor()

    return conn, cursor
