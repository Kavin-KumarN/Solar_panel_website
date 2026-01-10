from backend.database.db import get_db_connection


def get_active_testimonials():
    """
    Fetch all active testimonials for website display
    """
    connection = get_db_connection()
    if not connection:
        return []

    try:
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                id,
                customer_name,
                customer_type,
                review,
                rating,
                image_url,
                created_at
            FROM testimonials
            WHERE is_active = TRUE
            ORDER BY created_at DESC
        """

        cursor.execute(query)
        results = cursor.fetchall()

        return results

    except Exception as e:
        print(f"❌ Error fetching testimonials: {e}")
        return []

    finally:
        cursor.close()
        connection.close()
