from admissions import add_student
from deletions import delete_student
from lookup import search_student
from updates import update_student
from reports import generate_report
from file_handler import backup_csv
from bulk_import import bulk_import
from sorting_filtering import sort_students, filter_students

def clerk_menu():
    while True:
        print("\n--- CLERK MENU ---")
        print("1. Add student")
        print("2. Delete student")
        print("3. Bulk Import CSV")
        print("4. Backup CSV")
        print("5. Exit")
        ch = input("Choice: ").strip()
        if ch == '1':
            add_student()
        elif ch == '2':
            delete_student()
        elif ch == '3':
            path = input("Enter CSV file path to import: ").strip()
            imported, errors = bulk_import(path)
            print(f"Imported: {imported}, Errors: {errors}")
        elif ch == '4':
            path = backup_csv()
            print("Backup created:", path)
        elif ch == '5':
            break
        else:
            print("Invalid choice")

def teacher_menu():
    while True:
        print("\n--- TEACHER MENU ---")
        print("1. Search student")
        print("2. Update student marks/attendance")
        print("3. Sort students")
        print("4. Filter students")
        print("5. Exit")
        ch = input("Choice: ").strip()
        if ch == '1':
            search_student()
        elif ch == '2':
            update_student()
        elif ch == '3':
            field = input("Enter field to sort by (Roll_No, Name, Branch, Year, Attendance_%, Mid1_Marks,...): ").strip()
            students = sort_students(field)
            for s in students:
                print(s)
        elif ch == '4':
            branch = input("Filter by Branch (leave empty to skip): ").strip()
            year = input("Filter by Year (leave empty to skip): ").strip()
            students = filter_students(branch or None, year or None)
            for s in students:
                print(s)
        elif ch == '5':
            break
        else:
            print("Invalid choice")

def hod_menu():
    while True:
        print("\n--- HOD MENU ---")
        print("1. Generate report")
        print("2. Sort students")
        print("3. Filter students")
        print("4. Exit")
        ch = input("Choice: ").strip()
        if ch == '1':
            generate_report()
        elif ch == '2':
            field = input("Enter field to sort by (Roll_No, Name, Branch, Year, Attendance_%, Mid1_Marks,...): ").strip()
            students = sort_students(field)
            for s in students:
                print(s)
        elif ch == '3':
            branch = input("Filter by Branch (leave empty to skip): ").strip()
            year = input("Filter by Year (leave empty to skip): ").strip()
            students = filter_students(branch or None, year or None)
            for s in students:
                print(s)
        elif ch == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("Select your role:")
        print("1. Clerk")
        print("2. Teacher")
        print("3. HOD")
        print("4. Exit")
        role = input("Enter choice: ").strip()
        if role == '1':
            clerk_menu()
        elif role == '2':
            teacher_menu()
        elif role == '3':
            hod_menu()
        elif role == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice")
