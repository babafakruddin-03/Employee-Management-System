from db_connection import create_connection

connection = create_connection()

if connection:
    connection.close()
    print("Database connection closed.")
else:
    print("Please check your database connection settings.")