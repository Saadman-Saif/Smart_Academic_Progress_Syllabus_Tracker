from db import get_db

def create_ct_if_not_exists(user_email, course_code):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO ct_marks (user_email, course_code)
        VALUES (?, ?)
    """, (user_email, course_code))

    conn.commit()
    conn.close()

def update_ct_mark(user_email, course_code, ct_number, mark):
    conn = get_db()
    cursor = conn.cursor()

    query = f"""
        UPDATE ct_marks
        SET ct{ct_number} = ?
        WHERE user_email = ? AND course_code = ?
    """

    cursor.execute(query, (mark, user_email, course_code))
    conn.commit()
    conn.close()


def get_ct_marks(user_email, course_code):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ct1, ct2, ct3, ct4
        FROM ct_marks
        WHERE user_email = ? AND course_code = ?
    """, (user_email, course_code))

    row = cursor.fetchone()
    conn.close()

    return row