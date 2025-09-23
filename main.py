from models import Student
from file_handler import load_students, save_student

# Load existing students
students = load_students()
print("Loaded students:", [s.to_dict() for s in students])

# Add a new student
new_student = Student(roll_no=101, name="Ravi", branch="CSE", year=1,gender="female", attendance=90, mid1=45, mid2=50,final=199,quiz=67)
save_student(new_student)
print("New student saved!")