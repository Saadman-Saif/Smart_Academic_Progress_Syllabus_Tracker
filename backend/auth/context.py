from flask import Blueprint, request, jsonify, session
from db import get_db

context_bp = Blueprint("context", __name__)


@context_bp.route("/me", methods=["GET"])
def get_current_user():
    """Return the logged-in user's row from study.db (session cookie required)."""
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    conn = get_db()
    user = conn.execute(
        """
        SELECT id, username, email, university, department, year, semester
        FROM users
        WHERE id = ?
        """,
        (user_id,),
    ).fetchone()
    conn.close()

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(
        {
            "id": user["id"],
            "username": user["username"],
            "email": user["email"],
            "university": user["university"],
            "department": user["department"],
            "year": user["year"],
            "semester": user["semester"],
        }
    )

@context_bp.route("/set-academic-context", methods=["POST"])
def set_academic_context():
    data = request.json

    conn = get_db()
    conn.execute("""
        UPDATE users
        SET university = ?, department = ?, year = ?, semester = ?
        WHERE id = ?
    """, (
        data["university"],
        data["department"],
        data["year"],
        data["semester"],
        data["user_id"]
    ))
    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})
