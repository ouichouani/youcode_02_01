import psycopg2



host = "postgresql"

if __name__ == "__main__":
    host = "localhost"

def get_connection():

    connection = psycopg2.connect(
        host=host,
        port=5432,
        database="youcode_02_01",
        user="postgres",
        password="postgres"
    )

    print("Connected to PostgreSQL!")

    return connection
