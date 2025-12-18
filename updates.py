from file_handler import load_students, save_students, FIELDNAMES

def update_student():
    students = load_students()
    roll = input("Enter Roll No to update: ").strip()
    for i, s in enumerate(students):
        if s["Roll_No"] == roll:
            field = input(f"Field to update {FIELDNAMES}: ").strip()
            if field in FIELDNAMES:
                old_val = students[i][field]
                new_val = input(f"New value (old={old_val}): ").strip()
                students[i][field] = new_val
                save_students(students)
                print("Updated ✅")
            else:
                print("Invalid field")
            break
    else:
        print("Roll not found")
