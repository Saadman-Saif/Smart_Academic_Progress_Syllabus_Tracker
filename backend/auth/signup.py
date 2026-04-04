from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash
from db import get_db
import sqlite3

#  blueprint 
signup_bp = Blueprint("signup_bp", __name__)

@signup_bp.route("/signup", methods=["POST"])
def signup():
    
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 2. Validate input
    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    # 3. Hash the password
    hashed_password = generate_password_hash(password)

    conn = None
    try:
        conn =get_db()
        cursor = conn.cursor()
        
        # 4. Insert the new user
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username,email, hashed_password)
        )
        conn.commit()

        user_id = cursor.lastrowid
        session["user_id"] = user_id  # Store user_id in session after successful signup
        
        return jsonify({"message": "User registered successfully",
                        "user_id": user_id,
                        "username": username,
                        "email": email
                        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"message": "Email already exists"}), 409

    except sqlite3.OperationalError as e:
        return jsonify({"message": f"Database error: {str(e)}"}), 500
    
    finally:
        # 5. Ensure the connection is closed even if an error occurs
        if conn:
            conn.close()