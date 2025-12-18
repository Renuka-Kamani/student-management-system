from file_handler import load_students, save_students, FIELDNAMES

def input_student():
    students = load_students()
    roll = input("Enter Roll No: ").strip()
    if any(s["Roll_No"] == roll for s in students):
        print("Duplicate Roll_No!")
        return None
    return {
        "Roll_No": roll,
        "Name": input("Name: ").strip(),
        "Branch": input("Branch: ").strip(),
        "Year": input("Year: ").strip(),
        "Gender": input("Gender: ").strip(),
        "Age": input("Age: ").strip(),
        "Attendance_%": input("Attendance %: ").strip(),
        "Mid1_Marks": input("Mid1 Marks: ").strip(),
        "Mid2_Marks": input("Mid2 Marks: ").strip(),
        "Quiz_Marks": input("Quiz Marks: ").strip(),
        "Final_Marks": input("Final Marks: ").strip()
    }

def add_student():
    students = load_students()
    s = input_student()
    if s:
        students.append(s)
        save_students(students)
        print("Student added ✅")
