import mysql.connector
import  dbConnection as db
def connect_to_mysql():
    # Replace the following with your MySQL database information
    host = 'localhost'
    user = 'root'
    password = 'your password'
    database = 'database name'

    try:
        # Create a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print(f"Connected to MySQL database '{database}'")

            # Perform database operations here

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection in the finally block
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed")

# Call the function to connect to MySQL
connect_to_mysql()
