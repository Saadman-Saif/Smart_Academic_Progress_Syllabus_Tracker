from flask import Blueprint, request, jsonify
from db import get_db

syllabus_bp = Blueprint("syllabus", __name__)

# Get all subjects
@syllabus_bp.route("/subjects", methods=["GET"])
def get_subjects():
    conn = get_db()
    subjects = conn.execute("SELECT * FROM subjects").fetchall()
    conn.close()

    return jsonify([dict(row) for row in subjects])


# Get subject with progress
@syllabus_bp.route("/subject/<int:subject_id>/<int:user_id>", methods=["GET"])
def get_subject_progress(subject_id, user_id):

    conn = get_db()
    cursor = conn.cursor()

    topics = cursor.execute("""
        SELECT id, name FROM topics
        WHERE subject_id = ?
    """, (subject_id,)).fetchall()

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
    user_id = data["user_id"]
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