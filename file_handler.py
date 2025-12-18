import csv
import os
import shutil
import datetime
from models import CSV_FIELDS, Student

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CSV file paths
STUDENTS_FILE = os.path.join(BASE_DIR, "students.csv")
DELETED_FILE = os.path.join(BASE_DIR, "students_deleted.csv")

# 🔹 Expose FIELDNAMES for other modules
FIELDNAMES = CSV_FIELDS

# Ensure students.csv exists
if not os.path.exists(STUDENTS_FILE):
    with open(STUDENTS_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()

def load_students():
    """Load students from CSV as list of dictionaries"""
    with open(STUDENTS_FILE, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def save_students(students):
    """Save list of dictionaries to students.csv"""
    with open(STUDENTS_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(students)

def backup_csv():
    """Create timestamped backup of students.csv"""
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    target = os.path.join(BASE_DIR, f"students_backup_{ts}.csv")
    shutil.copy(STUDENTS_FILE, target)
    return target
