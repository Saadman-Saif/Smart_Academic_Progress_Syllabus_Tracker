from flask import Blueprint, request, jsonify
from db import get_auth_db

context_bp = Blueprint("context", __name__)

@context_bp.route("/set-academic-context", methods=["POST"])
def set_academic_context():
    data = request.json

    conn = get_auth_db()
    conn.execute("""
        UPDATE users
        SET university = ?, department = ?, year = ?, semester = ?
        WHERE email = ?
    """, (
        data["university"],
        data["department"],
        data["year"],
        data["semester"],
        data["email"]
    ))
    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})
