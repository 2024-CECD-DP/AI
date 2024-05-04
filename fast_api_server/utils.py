import config
import psycopg2


def get_db_connection():
    return psycopg2.connect(
        dbname=config.PostgresConfig.dbname,
        user=config.PostgresConfig.user,
        password=config.PostgresConfig.password,
        host=config.PostgresConfig.host,
        port=config.PostgresConfig.port
    )
