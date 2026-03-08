import json
import os
from db import get_db   

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# JSON_PATH = os.path.join(BASE_DIR, "2-2_CSE_RUET_syllabus_mainCopy.json")

def import_syllabus(json_filename, department, year, semester, university):
    JSON_PATH = os.path.join(BASE_DIR, json_filename)
    conn = get_db()
    cursor = conn.cursor()

    # Prevent duplicate import
    cursor.execute("""
            SELECT COUNT(*) FROM courses
            WHERE department = ? AND year = ? AND semester = ? AND university = ?
                   """, (department, year, semester, university))
    if cursor.fetchone()[0] > 0:
        print("Syllabus already imported.")
        conn.close()
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    for course in data:
        # Insert course 
        cursor.execute("""
            INSERT INTO courses (course_code, course_name, department, year, semester, university)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            course["course_code"],
            course["course_name"],
              department, 
              year, 
              semester, 
              university))

        course_id = cursor.lastrowid

        for module in course["modules"]:
            cursor.execute("""
            INSERT INTO modules (course_id, title)
            VALUES (?, ?)
        """, (course_id, module["title"]))
            module_id = cursor.lastrowid

            for topic in module["topics"]:
                cursor.execute("""
                    INSERT INTO topics (module_id, name)
                    VALUES (?, ?)
                """, (module_id, topic))

    conn.commit()
    conn.close()

    print("Syllabus imported successfully into study.db")