from load.connection import get_connection

connection = get_connection()
cursor = connection.cursor()


with open ("load/sql_files/schema.sql", "r") as file:
    sql = file.read()

cursor.execute(sql)
connection.commit()

cursor.close()
connection.close()

print("Disconnected from PostgreSQL!")
print("Tables created successfully!")