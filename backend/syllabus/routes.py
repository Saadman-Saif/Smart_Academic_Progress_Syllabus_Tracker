from flask import Blueprint, request, jsonify
from db import get_master_db, get_user_syllabus_db

syllabus_bp = Blueprint("syllabus", __name__)

def fetch_full_syllabus(conn, courses):
    result = []

    for course in courses:
        modules = conn.execute(
            "SELECT * FROM modules WHERE course_id = ?",
            (course["id"],)
        ).fetchall()

        module_list = []
        for module in modules:
            topics = conn.execute(
                "SELECT topic FROM topics WHERE module_id = ?",
                (module["id"],)
            ).fetchall()

            module_list.append({
                "title": module["title"],
                "topics": [t["topic"] for t in topics]
            })

        result.append({
            "course_code": course["course_code"],
            "course_name": course["course_name"],
            "credit_hour": course["credit_hour"],
            "modules": module_list
        })

    return result


@syllabus_bp.route("/get-syllabus", methods=["POST"])
def get_syllabus():
    data = request.json

    university = data["university"]
    year = data["year"]
    semester = data["semester"]

    # 1️⃣ Try user DB first
    user_db = get_user_syllabus_db()
    user_courses = user_db.execute("""
        SELECT * FROM courses
        WHERE university=? AND year=? AND semester=?
    """, (university, year, semester)).fetchall()

    if user_courses:
        result = fetch_full_syllabus(user_db, user_courses)
        user_db.close()
        return jsonify(result)

    user_db.close()
@syllabus_bp.route("/edit-topic", methods=["POST"])
def edit_topic():
    data = request.json

    course_code = data["course_code"]
    old_topic = data["old_topic"]
    new_topic = data["new_topic"]

    conn = get_user_syllabus_db()

    # Insert edited topic into USER DB
    conn.execute("""
        INSERT INTO topics (module_id, topic)
        VALUES (
            (
                SELECT m.id FROM modules m
                JOIN courses c ON m.course_id = c.id
                WHERE c.course_code = ?
                LIMIT 1
            ),
            ?
        )
    """, (course_code, new_topic))

    conn.commit()
    conn.close()

    return {"status": "saved_to_user_db"}

    # 2️⃣ Fallback to master DB
    master_db = get_master_db()
    master_courses = master_db.execute("""
        SELECT * FROM courses
        WHERE university=? AND year=? AND semester=?
    """, (university, year, semester)).fetchall()

    result = fetch_full_syllabus(master_db, master_courses)
    master_db.close()

    return jsonify(result)
