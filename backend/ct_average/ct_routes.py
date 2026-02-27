from flask import Blueprint, request, jsonify, session
from ct_average.ct_model import (
    create_ct_if_not_exists,
    update_ct_mark,
    get_ct_marks
)
from ct_average.ct_service import calculate_best_three


ct_bp = Blueprint("ct_bp", __name__)


@ct_bp.route("/ct/update", methods=["POST"])
def update_ct():
    data = request.json

    course_code = data.get("course_code")
    ct_number = data.get("ct_number")
    mark = data.get("mark")

    if not course_code:
        return jsonify({"error": "Course code required"}), 400

    if ct_number not in [1, 2, 3, 4]:
        return jsonify({"error": "Invalid CT number"}), 400

    if mark is None or mark < 0 or mark > 20:
        return jsonify({"error": "Invalid mark"}), 400

    email = session.get("user_email")
    if not email:
        return jsonify({"error": "Not logged in"}), 401

    create_ct_if_not_exists(email, course_code)
    update_ct_mark(email, course_code, ct_number, mark)

    marks_row = get_ct_marks(email, course_code)
    marks = list(marks_row) if marks_row else [None, None, None, None]

    avg, count = calculate_best_three(marks)

    return jsonify({
        "average": avg,
        "counted_ct": count
    })


@ct_bp.route("/ct/<course_code>", methods=["GET"])
def get_ct(course_code):
    email = session.get("user_email")
    if not email:
        return jsonify({"error": "Not logged in"}), 401

    create_ct_if_not_exists(email, course_code)

    marks_row = get_ct_marks(email, course_code)
    marks = list(marks_row) if marks_row else [None, None, None, None]

    avg, count = calculate_best_three(marks)

    return jsonify({
        "ct_marks": marks,
        "average": avg,
        "counted_ct": count
    })