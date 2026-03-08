import os
from import_syllabus import import_syllabus
from db import get_db

SYLLABUS_FOLDER = "syllabus_data"

def initialize_syllabus():

    conn = get_db()
    count = conn.execute("SELECT COUNT(*) FROM courses").fetchone()[0]
    conn.close()

    if count > 0:
        print("Syllabus already initialized.")
        return

    print("Importing syllabus files...")

    for filename in os.listdir(SYLLABUS_FOLDER):

        if filename.endswith(".json"):

            name = filename.replace(".json","")

            university, department, year, semester = name.split("_")

            import_syllabus(
                os.path.join(SYLLABUS_FOLDER, filename),
                department,
                int(year),
                int(semester),
                university
            )