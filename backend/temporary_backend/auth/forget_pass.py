from flask import Blueprint, request, jsonify 
from werkzeug.security import generate_password_hash
import random
import smtplib
from email.message import EmailMessage
from db import get_db
from datetime import datetime, timedelta

# Blueprint MUST be named password_bp
password_bp = Blueprint("password_bp", __name__)

#  EMAIL CONFIG 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "academicprogresstracker0@gmail.com"       #  change
SENDER_PASSWORD = "ufjagddzwuyfdwqr"     #  change

#  FORGOT PASSWORD 
@password_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    data = request.json
    email = data.get("email")

    if not email:
        return jsonify({"message": "Email required"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return jsonify({"message": "User not found"}), 404
    user_id = user["id"]
    # Generate reset code
    reset_code = str(random.randint(100000, 999999))

    # Insert reset request into password_resets table
    cursor.execute("""
        INSERT INTO password_resets (user_id, code)
        VALUES (?, ?)
    """, (user_id, reset_code))

    conn.commit()
    conn.close()

    send_email(email, reset_code)

    return jsonify({"message": "Reset code sent to email"}), 200


#RESET PASSWORD 
@password_bp.route("/reset-password", methods=["POST"])
def reset_password():
    data = request.json
    email = data.get("email")
    code = data.get("code")
    new_password = data.get("new_password")

    if not all([email, code, new_password]):
        return jsonify({"message": "All fields required"}), 400

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if not user:
        conn.close()
        return jsonify({"message": "User not found"}), 404

    user_id = user["id"]
    # Check for latest reset code
    cursor.execute("""
        SELECT code, created_at FROM password_resets
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT 1
    """, (user_id,))
    reset_request = cursor.fetchone()

    if not reset_request:
        conn.close()
        return jsonify({"message": "No reset request found"}), 404

    # Check code validity (10 minutes)
    if reset_request["code"] != code:
        conn.close()
        return jsonify({"message": "Invalid reset code"}), 401

    created_at = datetime.strptime(reset_request["created_at"], "%Y-%m-%d %H:%M:%S")

    if datetime.utcnow() > created_at + timedelta(minutes=10):
        conn.close()
        return jsonify({"message": "Reset code expired"}), 401

    # Update user password
    hashed_password = generate_password_hash(new_password)
    cursor.execute("""
        UPDATE users
        SET password = ?
        WHERE id = ?
    """, (hashed_password, user_id))

    # Optional: delete used reset codes
    cursor.execute("""
        DELETE FROM password_resets
        WHERE user_id = ?
    """, (user_id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Password updated successfully"}), 200


# ================= EMAIL FUNCTION =================
def send_email(to_email, code):
    msg = EmailMessage()
    msg["Subject"] = "Password Reset Code"
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg.set_content(f"You asked for resetting of your password for app.\
                    Here is your password reset code for it: {code}.\n \
                     If you didn't ask for it, please ignore this email.")

               
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)