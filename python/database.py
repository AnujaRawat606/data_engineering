import psycopg2


def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        database="ecommerce_analytics",
        user="anuja"
    )

    return connection