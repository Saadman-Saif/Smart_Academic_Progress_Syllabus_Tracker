from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash
from db import get_db

# 1. Define the Blueprint
login_bp = Blueprint("login_bp", __name__)
logout_bp = Blueprint("logout_bp", __name__)
session_bp = Blueprint("session_bp", __name__)
@login_bp.route("/login", methods=["POST"])
def login():
   
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    email = data.get("email") # Changed from username to email
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    conn = get_db()
    try:
        cursor = conn.cursor()
        # 3. Query the DB using email
        cursor.execute(
            "SELECT id, username, email, password FROM users WHERE email = ?",
            (email,),
        )
        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):
            session.permanent = True
            session["user_id"] = user["id"]
            cursor.execute(
            "UPDATE users SET is_logged_in = 1 WHERE id = ?",
            (user["id"],)
                )
            conn.commit()
            return jsonify(
                {
                    "message": "Login successful",
                    "user_id": user["id"],
                    "username": user["username"],
                    "email": user["email"],
                }
            ), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
            
    except Exception as e:
        return jsonify({"message": f"Server error: {str(e)}"}), 500
    finally:
        conn.close()
@logout_bp.route("/logout", methods=["POST"])
def logout():
    conn = get_db()
    cursor = conn.cursor()

    if "user_id" in session:
        cursor.execute(
            "UPDATE users SET is_logged_in = 0 WHERE id = ?",
            (session["user_id"],)
        )
        conn.commit()

    session.clear()
    conn.close()

    return jsonify({"message": "Logout successful"}), 200

@session_bp.route("/check-session", methods=["GET"])
def check_session():
    if "user_id" not in session:
        return jsonify({"logged_in": False}), 401

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT is_logged_in FROM users WHERE id = ?",
        (session["user_id"],)
    )
    user = cursor.fetchone()
    conn.close()

    if user and user["is_logged_in"] == 1:
        return jsonify({
            "logged_in": True,
            "user_id": session["user_id"]
        }), 200

    return jsonify({"logged_in": False}), 401