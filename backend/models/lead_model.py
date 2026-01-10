from backend.database.db import get_db_connection


def create_lead(name, phone, email, location, user_type, message=None):
    """
    Insert a new lead into the database
    """
    connection = get_db_connection()
    if not connection:
        return False

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO leads (name, phone, email, location, user_type, message)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (name, phone, email, location, user_type, message)

        cursor.execute(query, values)
        connection.commit()

        return True

    except Exception as e:
        print(f"❌ Error inserting lead: {e}")
        return False

    finally:
        cursor.close()
        connection.close()


def get_all_leads():
    """
    Fetch all leads (for admin or analytics)
    """
    connection = get_db_connection()
    if not connection:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                id,
                name,
                phone,
                email,
                location,
                user_type,
                message,
                created_at
            FROM leads
            ORDER BY created_at DESC
        """

        cursor.execute(query)
        results = cursor.fetchall()

        return results

    except Exception as e:
        print(f"❌ Error fetching leads: {e}")
        return []

    finally:
        cursor.close()
        connection.close()

# if __name__ == "__main__":
#     success = create_lead(
#         name="Test User",
#         phone="9999999999",
#         email="test@example.com",
#         location="Chennai",
#         user_type="Residential",
#         message="Test lead from model"
#     )
#
#     if success:
#         print("✅ Lead inserted successfully")
#     else:
#         print("❌ Lead insertion failed")
#
#     leads = get_all_leads()
#     print(f"Total leads in DB: {len(leads)}")
