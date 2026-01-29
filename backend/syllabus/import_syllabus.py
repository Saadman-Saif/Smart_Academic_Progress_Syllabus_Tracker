import json
import sqlite3

conn = sqlite3.connect("syllabus.db")
c = conn.cursor()

# Create tables
c.execute("""
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

c.execute("""
CREATE TABLE IF NOT EXISTS modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    title TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER,
    topic TEXT
)
""")

# Load JSON
with open("syllabus/2-2syllabus_mainCopy.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for course in data:
    c.execute("""
        INSERT INTO courses 
        (course_code, course_name, credit_hour, year, semester, university)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        course["course_code"],
        course["course_name"],
        course["credit_hour"],
        2,
        2,
        "RUET"
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

print("✅ Syllabus imported successfully")
