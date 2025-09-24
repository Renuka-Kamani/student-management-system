import csv
from models import Student

STUDENTS_FILE = 'students.csv'

def save_students_to_csv(students):
    try:
        with open(STUDENTS_FILE, mode='w', newline='') as file:
            columnnames = ["Roll_No", "Name", "Age", "Year", "Gender", "Mid1_Marks", "Mid2_Marks", "Final_Marks", "Quiz_Marks", "Attendence_%"]
            writer = csv.DictWriter(file, columnnames=columnnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student.to_dic())
    except IOError as e:
        print(f"Error saving file: {e}")

def load_students_from_csv():
    """Loads student data from a CSV file and returns a list of Student objects."""
    students = []
    try:
        with open(STUDENTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Create a Student object from each row
                    student = Student(
                        attendence=row["Attendence_%"],
                        name=row["Name"],
                        roll_no=row["Roll_No"],
                        year=row["Year"],
                        gender=row["Gender"],
                        age=row["Age"],
                        mid_1=row["Mid1_Marks"],
                        mid_2=row["Mid2_Marks"],
                        final=row["Final_Marks"],
                        quiz=row["Quiz_Marks"]
                    )
                    students.append(student)
                except (ValueError, KeyError) as e:
                    print(f"Error loading student record from CSV: {e}. Skipping row.")
    except FileNotFoundError:
        print("students.csv not found. Starting with an empty student list.")
    except IOError as e:
        print(f"Error reading file: {e}")
    return students