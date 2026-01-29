from flask import Blueprint, request, jsonify

# DB helpers
from db import (
    get_auth_db,
    get_master_db,
    get_user_syllabus_db
)
syllabus_bp = Blueprint("syllabus", __name__)

# ============================================================
# HELPERS (READ-ONLY / PROCESSING ONLY)
# ============================================================

def get_user_context(email):
    """
    Fetch user's academic context from users.db
    """
    conn = get_auth_db()
    user = conn.execute("""
        SELECT university, department, year, semester
        FROM users
        WHERE email = ?
    """, (email,)).fetchone()
    conn.close()
    return user


def load_master_syllabus(university, year, semester):
    """
    Load full syllabus from syllabus_main.db
    """
    conn = get_master_db()

    courses = conn.execute("""
        SELECT * FROM courses
        WHERE university = ? AND year = ? AND semester = ?
    """, (university, year, semester)).fetchall()

    syllabus = []

    for course in courses:
        modules = conn.execute("""
            SELECT * FROM modules
            WHERE course_id = ?
        """, (course["id"],)).fetchall()

        module_list = []
        for module in modules:
            topics = conn.execute("""
                SELECT topic FROM topics
                WHERE module_id = ?
            """, (module["id"],)).fetchall()

            module_list.append({
                "title": module["title"],
                "topics": [t["topic"] for t in topics]
            })

        syllabus.append({
            "course_code": course["course_code"],
            "course_name": course["course_name"],
            "credit_hour": course["credit_hour"],
            "modules": module_list
        })

    conn.close()
    return syllabus


def load_user_overrides(email):
    """
    Load topic overrides from syllabus_user.db
    """
    conn = get_user_syllabus_db()
    rows = conn.execute("""
        SELECT course_code, module_title, original_topic, modified_topic
        FROM topic_overrides
        WHERE user_email = ?
    """, (email,)).fetchall()
    conn.close()

    overrides = {}
    for row in rows:
        key = (
            row["course_code"],
            row["module_title"],
            row["original_topic"]
        )
        overrides[key] = row["modified_topic"]

    return overrides


def merge_syllabus(master_syllabus, overrides):
    """
    Merge master syllabus with user overrides
    """
    for course in master_syllabus:
        for module in course["modules"]:
            merged_topics = []

            for topic in module["topics"]:
                key = (
                    course["course_code"],
                    module["title"],
                    topic
                )

                if key in overrides:
                    merged_topics.append({
                        "name": overrides[key],
                        "is_custom": True
                    })
                else:
                    merged_topics.append({
                        "name": topic,
                        "is_custom": False
                    })

            module["topics"] = merged_topics

    return master_syllabus

# ============================================================
# ROUTES
# ============================================================

@syllabus_bp.route("/get-syllabus", methods=["POST"])
def get_syllabus():
    """
    Return FULL syllabus (master + user overrides merged)
    """
    email = request.json.get("email")

    if not email:
        return jsonify({"error": "Email required"}), 400

    # 1️⃣ Get academic context
    context = get_user_context(email)
    if not context or not context["university"]:
        return jsonify({"error": "Academic context not set"}), 400

    # 2️⃣ Load master syllabus
    master_syllabus = load_master_syllabus(
        context["university"],
        context["year"],
        context["semester"]
    )

    # 3️⃣ Load user overrides
    overrides = load_user_overrides(email)

    # 4️⃣ Merge
    final_syllabus = merge_syllabus(master_syllabus, overrides)

    return jsonify(final_syllabus)


@syllabus_bp.route("/edit-topic", methods=["POST"])
def edit_topic():
    """
    Save/replace a topic override in syllabus_user.db
    """
    data = request.json

    required_fields = [
        "email",
        "course_code",
        "module_title",
        "original_topic",
        "modified_topic"
    ]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    conn = get_user_syllabus_db()

    # Remove existing override if any
    conn.execute("""
        DELETE FROM topic_overrides
        WHERE user_email = ?
          AND course_code = ?
          AND module_title = ?
          AND original_topic = ?
    """, (
        data["email"],
        data["course_code"],
        data["module_title"],
        data["original_topic"]
    ))

    # Insert new override
    conn.execute("""
        INSERT INTO topic_overrides
        (user_email, course_code, module_title, original_topic, modified_topic)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["email"],
        data["course_code"],
        data["module_title"],
        data["original_topic"],
        data["modified_topic"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})


@syllabus_bp.route("/reset-topic", methods=["POST"])
def reset_topic():
    """
    Reset a topic back to master syllabus
    """
    data = request.json

    required_fields = [
        "email",
        "course_code",
        "module_title",
        "original_topic"
    ]

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    conn = get_user_syllabus_db()
    conn.execute("""
        DELETE FROM topic_overrides
        WHERE user_email = ?
          AND course_code = ?
          AND module_title = ?
          AND original_topic = ?
    """, (
        data["email"],
        data["course_code"],
        data["module_title"],
        data["original_topic"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"status": "reset"})


@syllabus_bp.route("/my-changes", methods=["POST"])
def my_changes():
    """
    Return ONLY user changes (optional menu feature)
    """
    email = request.json.get("email")

    if not email:
        return jsonify({"error": "Email required"}), 400

    conn = get_user_syllabus_db()
    rows = conn.execute("""
        SELECT course_code, module_title, original_topic, modified_topic, created_at
        FROM topic_overrides
        WHERE user_email = ?
    """, (email,)).fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])
