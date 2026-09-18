import psycopg2

def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="youcode_02_01",
        user="postgres",
        password="postgres"
    )

    print("Connected to PostgreSQL!")

    return connection
