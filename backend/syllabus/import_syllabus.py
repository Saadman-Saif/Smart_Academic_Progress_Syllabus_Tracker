import json
import sqlite3
import os

# ---------------- CONFIG (CHANGE ONLY THESE) ----------------
UNIVERSITY = "RUET"
YEAR = 2
SEMESTER = 2
JSON_FILE = "2-2_CSE_RUET_syllabus_mainCopy.json"
# ------------------------------------------------------------

# Absolute paths (SAFE)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "syllabus_main.db")
JSON_PATH = os.path.join(BASE_DIR, JSON_FILE)

# Connect to MASTER syllabus DB
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# ---------------- CREATE TABLES (MASTER ONLY) ----------------

c.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT NOT NULL,
    course_name TEXT NOT NULL,
    credit_hour REAL,
    year INTEGER NOT NULL,
    semester INTEGER NOT NULL,
    university TEXT NOT NULL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id)
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    topic TEXT NOT NULL,
    FOREIGN KEY (module_id) REFERENCES modules(id)
)
""")

# ---------------- LOAD JSON ----------------

if not os.path.exists(JSON_PATH):
    raise FileNotFoundError(f"JSON file not found: {JSON_PATH}")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---------------- INSERT DATA ----------------

for course in data:
    c.execute("""
        INSERT INTO courses
        (course_code, course_name, credit_hour, year, semester, university)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        course["course_code"],
        course["course_name"],
        course.get("credit_hour"),
        YEAR,
        SEMESTER,
        UNIVERSITY
    ))

    course_id = c.lastrowid

    for module in course["modules"]:
        c.execute("""
            INSERT INTO modules (course_id, title)
            VALUES (?, ?)
        """, (course_id, module["title"]))

        module_id = c.lastrowid

        for topic in module["topics"]:
            c.execute("""
                INSERT INTO topics (module_id, topic)
                VALUES (?, ?)
            """, (module_id, topic))

conn.commit()
conn.close()

print("MASTER syllabus imported successfully")
print(f"   University : {UNIVERSITY}")
print(f"   Year       : {YEAR}")
print(f"   Semester   : {SEMESTER}")
