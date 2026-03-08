from flask import session
from flask import Blueprint, request, jsonify
from session_tracker.services.study_timer_service import StudyTimerService

study_timer_bp = Blueprint("study_timer", __name__)
service = StudyTimerService()


@study_timer_bp.route("/study/start", methods=["POST"])
def start_study():
    try:
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"error": "Not logged in"}), 401

        session_id = service.start_session(user_id)
        return jsonify({"session_id": session_id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@study_timer_bp.route("/study/pause", methods=["POST"])
def pause_study():
    try:
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"error": "Not logged in"}), 401
        service.pause_session(user_id)
        return jsonify({"message": "Study session paused"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@study_timer_bp.route("/study/resume", methods=["POST"])
def resume_study():
    try:
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"error": "Not logged in"}), 401
        
        service.resume_session(user_id)
        return jsonify({"message": "Study session resumed"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@study_timer_bp.route("/study/stop", methods=["POST"])
def stop_study():
    try:
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"error": "Not logged in"}), 401
        data = request.get_json(silent=True) or {}
        interrupted = bool(data.get("interrupted", False))
        service.stop_session(user_id, interrupted=interrupted)
        return jsonify({"message": "Study session stopped"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@study_timer_bp.route("/study/today-summary", methods=["GET"])
def today_summary():
    try:
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"error": "Not logged in"}), 401
        summary = service.get_today_summary(user_id)
        return jsonify(summary), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
