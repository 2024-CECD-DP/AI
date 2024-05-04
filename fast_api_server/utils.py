from config import PostgresConfig
import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        dbname=PostgresConfig.dbname,
        user=PostgresConfig.user,
        password=PostgresConfig.password,
        host=PostgresConfig.host,
        port=PostgresConfig.port
    )
    cur = conn.cursor()
    return conn, cur
