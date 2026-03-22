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


def _syllabus_hierarchy_for_user(conn, user_id, university, department, year, semester):
    """
    Mirrors the JSON syllabus shape: list of courses, each with modules and topics.
    DB-backed ids are included on courses, modules, and topics; topics also include
    completion for the given user (not in the original JSON, but needed for the app).
    """
    courses = conn.execute(
        """
        SELECT id, course_code, course_name, department, year, semester, university
        FROM courses
        WHERE university = ? AND department = ? AND year = ? AND semester = ?
        ORDER BY id
        """,
        (university, department, year, semester),
    ).fetchall()

    if not courses:
        return []

    course_ids = [c["id"] for c in courses]
    ph_c = ",".join("?" * len(course_ids))
    modules = conn.execute(
        f"""
        SELECT id, course_id, title
        FROM modules
        WHERE course_id IN ({ph_c})
        ORDER BY course_id, id
        """,
        course_ids,
    ).fetchall()

    modules_by_course = {}
    module_ids = []
    for m in modules:
        modules_by_course.setdefault(m["course_id"], []).append(m)
        module_ids.append(m["id"])

    topic_completion = {}
    topics_by_module = {}
    if module_ids:
        ph_m = ",".join("?" * len(module_ids))
        topics = conn.execute(
            f"""
            SELECT id, module_id, name
            FROM topics
            WHERE module_id IN ({ph_m})
            ORDER BY module_id, id
            """,
            module_ids,
        ).fetchall()
        topic_ids = [t["id"] for t in topics]
        for t in topics:
            topics_by_module.setdefault(t["module_id"], []).append(t)

        if topic_ids:
            ph_t = ",".join("?" * len(topic_ids))
            rows = conn.execute(
                f"""
                SELECT topic_id, completed
                FROM completions
                WHERE user_id = ? AND topic_id IN ({ph_t})
                """,
                [user_id] + topic_ids,
            ).fetchall()
            topic_completion = {r["topic_id"]: bool(r["completed"]) for r in rows}

    result = []
    for c in courses:
        mod_list = []
        for m in modules_by_course.get(c["id"], []):
            topic_list = []
            for t in topics_by_module.get(m["id"], []):
                topic_list.append(
                    {
                        "id": t["id"],
                        "name": t["name"],
                        "completed": topic_completion.get(t["id"], False),
                    }
                )
            mod_list.append({"id": m["id"], "title": m["title"], "topics": topic_list})
        result.append(
            {
                "id": c["id"],
                "course_code": c["course_code"],
                "course_name": c["course_name"],
                "department": c["department"],
                "year": c["year"],
                "semester": c["semester"],
                "university": c["university"],
                "modules": mod_list,
            }
        )
    return result


@syllabus_bp.route("/syllabus", methods=["GET"])
def get_full_syllabus():
    """Full course → module → topic tree for the logged-in user's program."""
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    conn = get_db()
    user = conn.execute(
        """
        SELECT university, department, year, semester
        FROM users
        WHERE id = ?
        """,
        (user_id,),
    ).fetchone()

    if not user:
        conn.close()
        return jsonify({"error": "User not found"}), 404

    hierarchy = _syllabus_hierarchy_for_user(
        conn,
        user_id,
        user["university"],
        user["department"],
        user["year"],
        user["semester"],
    )
    conn.close()
    return jsonify(hierarchy)


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