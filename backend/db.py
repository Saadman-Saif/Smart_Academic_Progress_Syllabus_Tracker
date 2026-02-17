import sqlite3
import os

# Base directory (path-safe for all OS)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



# AUTH DATABASE (users.db)
AUTH_DB = os.path.join(BASE_DIR, "users.db")

def get_auth_db():
    conn = sqlite3.connect(AUTH_DB, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def init_auth_db():
    conn = get_auth_db()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            username TEXT UNIQUE NOT NULL,
            university TEXT,
            department TEXT,
            year INTEGER,
            semester INTEGER
        )
    """)

    # Password reset table
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


# ============================================================
# MASTER SYLLABUS DATABASE (syllabus_main.db) – READ ONLY
# ============================================================
MASTER_DB = os.path.join(BASE_DIR, "syllabus_main.db")

def get_master_db():
    conn = sqlite3.connect(MASTER_DB)
    conn.row_factory = sqlite3.Row
    return conn


# ============================================================
# USER SYLLABUS DATABASE (syllabus_user.db) – OVERRIDES ONLY
# ============================================================
USER_SYLLABUS_DB = os.path.join(BASE_DIR, "syllabus_user.db")

def get_user_syllabus_db():
    conn = sqlite3.connect(USER_SYLLABUS_DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_user_syllabus_db():
    conn = get_user_syllabus_db()
    cursor = conn.cursor()

    # ONLY store user modifications (diffs)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topic_overrides (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            course_code TEXT NOT NULL,
            module_title TEXT NOT NULL,
            original_topic TEXT NOT NULL,
            modified_topic TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

# STUDY DATABASE (study.db)

STUDY_DB = os.path.join(BASE_DIR, "study.db")

def get_study_db():
    conn = sqlite3.connect(STUDY_DB, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn
def init_study_db():
    conn = get_study_db()
    cursor = conn.cursor()

    # Stores completed / interrupted sessions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_session (
            session_id TEXT PRIMARY KEY,
            date TEXT NOT NULL,
            start_ts INTEGER NOT NULL,
            end_ts INTEGER,
            planned_duration INTEGER NOT NULL,
            actual_duration INTEGER,
            status TEXT NOT NULL
        )
    """)

    # Stores currently running session (max ONE row)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS running_session (
            session_id TEXT PRIMARY KEY,
            start_ts INTEGER NOT NULL,
            planned_duration INTEGER NOT NULL,
            total_paused INTEGER DEFAULT 0,
            last_pause_ts INTEGER,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


init_auth_db()
init_user_syllabus_db()
init_study_db()