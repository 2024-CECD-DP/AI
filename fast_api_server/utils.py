from config import PostgresConfig
import psycopg2


def get_db_connection():
    return psycopg2.connect(
        dbname=PostgresConfig.dbname,
        user=PostgresConfig.user,
        password=PostgresConfig.password,
        host=PostgresConfig.host,
        port=PostgresConfig.port
    )
