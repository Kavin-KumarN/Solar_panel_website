import mysql.connector
from mysql.connector import Error
from backend.config import Config


def get_db_connection():
    """
    Creates and returns a MySQL database connection
    """
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            database=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )

        if connection.is_connected():
            return connection

    except Error as e:
        print(f"❌ Database connection error: {e}")
        return None

# if __name__ == "__main__":
#     conn = get_db_connection()
#     if conn:
#         print("✅ MySQL connection successful")
#         conn.close()
#     else:
#         print("❌ MySQL connection failed")
