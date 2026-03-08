from flask import Blueprint, request, jsonify, session
from db import get_db

syllabus_bp = Blueprint("syllabus", __name__)

# Get all courses
@syllabus_bp.route("/courses", methods=["GET"])
def get_courses():

    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    conn = get_db()

    user = conn.execute("""
        SELECT university, department, year, semester
        FROM users
        WHERE id = ?
    """, (user_id,)).fetchone()

    if not user:
        conn.close()
        return jsonify({"error": "User not found"}), 404

    courses = conn.execute("""
        SELECT *
        FROM courses
        WHERE university = ?
        AND department = ?
        AND year = ?
        AND semester = ?
    """, (
        user["university"],
        user["department"],
        user["year"],
        user["semester"]
    )).fetchall()

    conn.close()

    return jsonify([
        {
            "id": row["id"],
            "course_code": row["course_code"],
            "course_name": row["course_name"],
            "year": row["year"],
            "semester": row["semester"]
        }
        for row in courses
    ])

# Get course with progress
@syllabus_bp.route("/course/<int:course_id>", methods=["GET"])
def get_course_progress(course_id):
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not logged in"}), 401
    conn = get_db()
    cursor = conn.cursor()

    topics = cursor.execute("""
        SELECT topics.id, topics.name FROM topics
        JOIN modules ON topics.module_id = modules.id
        WHERE modules.course_id = ?
    """, (course_id,)).fetchall()

    total_topics = len(topics)
    completed_count = 0
    topic_list = []

    for topic in topics:
        row = cursor.execute("""
            SELECT completed FROM completions
            WHERE user_id = ? AND topic_id = ?
        """, (user_id, topic["id"])).fetchone()

        is_completed = row["completed"] if row else 0

        if is_completed:
            completed_count += 1

        topic_list.append({
            "id": topic["id"],
            "name": topic["name"],
            "completed": bool(is_completed)
        })

    percentage = (completed_count / total_topics * 100) if total_topics > 0 else 0

    conn.close()

    return jsonify({
        "total_topics": total_topics,
        "completed": completed_count,
        "percentage": round(percentage, 2),
        "topics": topic_list
    })


# Update completion
@syllabus_bp.route("/update-completion", methods=["POST"])
def update_completion():

    data = request.json
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not logged in"}), 401
    topic_id = data["topic_id"]
    completed = 1 if data["completed"] else 0

    conn = get_db()
    cursor = conn.cursor()

    existing = cursor.execute("""
        SELECT id FROM completions
        WHERE user_id = ? AND topic_id = ?
    """, (user_id, topic_id)).fetchone()

    if existing:
        cursor.execute("""
            UPDATE completions
            SET completed = ?
            WHERE user_id = ? AND topic_id = ?
        """, (completed, user_id, topic_id))
    else:
        cursor.execute("""
            INSERT INTO completions (user_id, topic_id, completed)
            VALUES (?, ?, ?)
        """, (user_id, topic_id, completed))

    conn.commit()
    conn.close()

    return jsonify({"status": "updated"})