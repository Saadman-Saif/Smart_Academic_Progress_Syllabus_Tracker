import sqlite3
import os

# Base directory (important for path safety)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- AUTH DATABASE ----------
AUTH_DB = os.path.join(BASE_DIR, "users.db")

def get_auth_db():
    conn = sqlite3.connect(AUTH_DB, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def init_auth_db():
    conn = get_auth_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_resets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            code TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# ---------- SYLLABUS MASTER DATABASE ----------
MASTER_DB = os.path.join(BASE_DIR, "syllabus_main.db")

def get_master_db():
    conn = sqlite3.connect(MASTER_DB)
    conn.row_factory = sqlite3.Row
    return conn

# ---------- SYLLABUS USER DATABASE ----------
USER_SYLLABUS_DB = os.path.join(BASE_DIR, "syllabus_user.db")

def get_user_syllabus_db():
    conn = sqlite3.connect(USER_SYLLABUS_DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_user_syllabus_db():
    conn = get_user_syllabus_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT,
            course_name TEXT,
            credit_hour REAL,
            year INTEGER,
            semester INTEGER,
            university TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS modules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER,
            title TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            module_id INTEGER,
            topic TEXT
        )
    """)

    conn.commit()
    conn.close()

# ---------- INITIALIZE DATABASES ----------
init_auth_db()
init_user_syllabus_db()
