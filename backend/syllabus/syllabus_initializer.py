import os
from syllabus.import_syllabus import import_syllabus
from db import get_db

SYLLABUS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "syllabus_data")

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

            name = filename.replace(".json", "")

            # e.g. RUET_CSE_2-2 -> university, department, year-semester (3 parts, not 4)
            university, department, year_semester = name.split("_", 2)
            year, semester = year_semester.split("-", 1)

            import_syllabus(
                os.path.join(SYLLABUS_FOLDER, filename),
                department,
                int(year),
                int(semester),
                university
            )