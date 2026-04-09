import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from db import get_db

routine_bp = Blueprint("routine", __name__)

UPLOAD_FOLDER = "uploads/routines"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "pdf"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@routine_bp.route("/routine/upload", methods=["POST"])
def upload_routine():
    try:
        user_id = request.form.get("user_id")

        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            ext = filename.rsplit(".", 1)[1].lower()
            file_type = "pdf" if ext == "pdf" else "image"

            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)

            conn = get_db()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO routine (user_id, file_name, file_path, file_type)
                VALUES (?, ?, ?, ?)
            """, (user_id, filename, save_path, file_type))

            conn.commit()

            return jsonify({
                "message": "Routine uploaded successfully",
                "file_path": save_path,
                "file_type": file_type
            }), 200

        return jsonify({"error": "Invalid file type"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@routine_bp.route("/routine/<int:user_id>", methods=["GET"])
def get_routine(user_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT file_name, file_path, file_type
        FROM routine
        WHERE user_id = ?
        ORDER BY uploaded_at DESC
        LIMIT 1
    """, (user_id,))

    routine = cursor.fetchone()

    if routine:
        return jsonify({
            "file_name": routine["file_name"],
            "file_path": routine["file_path"],
            "file_type": routine["file_type"]
        })

    return jsonify({"message": "No routine found"}), 404