

from file_handler import save_students_to_csv, load_students_from_csv
from models import Student
def add_new_student():
    try:
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        year = int(input("Enter Year: "))
        gender = input("Enter Gender: ")
        mid_1 = int(input("Enter Mid1 Marks: "))
        mid_2 = int(input("Enter Mid2 Marks: "))
        final = float(input("Enter Final Marks: "))
        quiz = float(input("Enter Quiz Marks: "))
        attendence = float(input("Enter Attendance %: "))

        new_student = Student(
            attendence=attendence,
            name=name,
            roll_no=roll_no,
            year=year,
            gender=gender,
            age=age,
            mid_1=mid_1,
            mid_2=mid_2,
            final=final,
            quiz=quiz
        )

        students_list = load_students_from_csv()
        students_list.append(new_student)
        save_students_to_csv(students_list)
        print("Student was added successfully!")

    except ValueError as e:
        print(f"Error: {e}. Please try again.")
    except Exception as e:
        print(f"Unexpected error: {e}")
