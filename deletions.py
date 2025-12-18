import csv
from file_handler import load_students, save_students, DELETED_FILE, FIELDNAMES

def delete_student():
    students = load_students()
    roll = input("Roll No to delete: ").strip()
    found = [s for s in students if s["Roll_No"] == roll]
    if found:
        students = [s for s in students if s["Roll_No"] != roll]
        save_students(students)
        with open(DELETED_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(found[0])
        print("Student deleted ✅")
    else:
        print("Roll not found")
