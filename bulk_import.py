# bulk_import.py
import csv, os
from models import Student
from file_handler import STUDENTS_FILE, FIELDNAMES, load_students, save_students

ERROR_FILE = os.path.join(os.path.dirname(STUDENTS_FILE), "import_errors.csv")

def is_valid(student: dict):
    try:
        if not student["Roll_No"]: return False
        if not student["Name"]: return False
        if float(student["Attendance_%"]) < 0 or float(student["Attendance_%"]) > 100: return False
        for f in ["Mid1_Marks","Mid2_Marks","Quiz_Marks","Final_Marks"]:
            if student[f] and (float(student[f]) < 0 or float(student[f]) > 100):
                return False
    except:
        return False
    return True

def bulk_import(file_path):
    students = load_students()
    existing_rolls = {s["Roll_No"] for s in students}
    imported, errors = [], []

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Roll_No"] in existing_rolls or not is_valid(row):
                errors.append(row)
            else:
                students.append(Student(**row).to_dict())
                imported.append(row)

    save_students(students)

    if errors:
        with open(ERROR_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerows(errors)

    return len(imported), len(errors)