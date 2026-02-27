from flask import Blueprint, request, jsonify, session
from werkzeug.security import check_password_hash
from db import get_auth_db

# 1. Define the Blueprint (This is what main.py is looking for)
login_bp = Blueprint("login_bp", __name__)

@login_bp.route("/login", methods=["POST"])
def login():
    # 2. Check if request is JSON
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    email = data.get("email") # Changed from username to email to match your DB
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    conn = get_auth_db()
    try:
        cursor = conn.cursor()
        # 3. Query the DB using email
        cursor.execute(
            "SELECT password FROM users WHERE email = ?", 
            (email,)
        )
        user = cursor.fetchone()
        
        # 4. Verify password hash
        if user and check_password_hash(user["password"], password):
           session["user_email"] = email #storing email in session
           return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401
            
    except Exception as e:
        return jsonify({"message": f"Server error: {str(e)}"}), 500
    finally:
        conn.close()