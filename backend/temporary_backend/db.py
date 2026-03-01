import sqlite3
import os

# Base directory (path-safe for all OS)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "study.db")

def get_db():
    conn = sqlite3.connect(DATABASE, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_db()
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
            semester INTEGER,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Password reset table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS password_resets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            code TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)
    #Subjects
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            university TEXT NOT NULL,
            department TEXT NOT NULL,
            year INTEGER NOT NULL,
            semester INTEGER NOT NULL
        )
    """)
    #Topics
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY(subject_id) REFERENCES subjects(id) ON DELETE CASCADE
        )
    """)
#Completion(User progress)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS completions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic_id INTEGER NOT NULL,
            completed INTEGER DEFAULT 0,
            UNIQUE(user_id, topic_id),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY(topic_id) REFERENCES topics(id) ON DELETE CASCADE
        )
    """)
    # ONLY store user modifications
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topic_overrides (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic_id INTEGER NOT NULL,
            modified_name TEXT NOT NULL,
            previous_name TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY(topic_id) REFERENCES topics(id) ON DELETE CASCADE
        )
    """)
    # Stores completed / interrupted sessions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_session (
            session_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            start_ts INTEGER NOT NULL,
            end_ts INTEGER,
            planned_duration INTEGER NOT NULL,
            actual_duration INTEGER,
            status TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE   
        )
    """)

    # Stores currently running session (max ONE row)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS running_session (
            session_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL UNIQUE,
            start_ts INTEGER NOT NULL,
            planned_duration INTEGER NOT NULL,
            total_paused INTEGER DEFAULT 0,
            last_pause_ts INTEGER,
            status TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)
    #stores CT table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ct_marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            course_code TEXT NOT NULL,
            ct1 INTEGER,
            ct2 INTEGER,
            ct3 INTEGER,
            ct4 INTEGER,
            UNIQUE(user_id, course_code),
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )
""")
    conn.commit()
    conn.close()
def ensure_syllabus_imported():
    from syllabus.import_syllabus import import_syllabus
    import_syllabus()
init_db()
ensure_syllabus_imported()