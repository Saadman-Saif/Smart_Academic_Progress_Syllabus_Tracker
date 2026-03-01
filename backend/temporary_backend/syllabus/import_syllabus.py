import json
import os
from db import get_db   

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "2-2_CSE_RUET_syllabus_mainCopy.json")

def import_syllabus():

    conn = get_db()
    cursor = conn.cursor()

    # Prevent duplicate import
    cursor.execute("SELECT COUNT(*) FROM subjects")
    if cursor.fetchone()[0] > 0:
        print("Syllabus already imported.")
        conn.close()
        return

    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    for course in data:
        # Insert course as subject
        cursor.execute("""
            INSERT INTO subjects (name,university, department, year, semester)
            VALUES (?, ?, ?, ?, ?)
        """, (f"{course['course_code']} - {course['course_name']}","RUET", "CSE", 2, 2))

        subject_id = cursor.lastrowid

        for module in course["modules"]:
            for topic in module["topics"]:
                full_topic_name = f"{module['title']} - {topic}"

                cursor.execute("""
                    INSERT INTO topics (subject_id, name)
                    VALUES (?, ?)
                """, (subject_id, full_topic_name))

    conn.commit()
    conn.close()

    print("Syllabus imported successfully into study.db")