from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from db import get_db
import sqlite3

# Define the blueprint to be imported in main.py
signup_bp = Blueprint("signup_bp", __name__)

@signup_bp.route("/signup", methods=["POST"])
def signup():
    # 1. Check if the request is JSON
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # 2. Validate input
    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    # 3. Hash the password for security
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
        return jsonify({""
            "message": "User registered successfully",
            "user_id": user_id
        }), 201

    except sqlite3.IntegrityError:
        # This triggers if the email already exists (UNIQUE constraint)
        return jsonify({"message": "Email already exists"}), 409

    except sqlite3.OperationalError as e:
        # Handles database-specific errors (like missing tables)
        return jsonify({"message": f"Database error: {str(e)}"}), 500
    
    finally:
        # 5. Ensure the connection is closed even if an error occurs
        if conn:

            conn.close()
