from dataclasses import dataclass, asdict

CSV_FIELDS = [
    'Roll_No','Name','Branch','Year','Gender','Age',
    'Attendance_Percent','Mid1_Marks','Mid2_Marks','Quiz_Marks','Final_Marks'
]

@dataclass
class Student:
    Roll_No: str
    Name: str
    Branch: str
    Year: str
    Gender: str
    Age: str
    Attendance_Percent: str
    Mid1_Marks: str
    Mid2_Marks: str
    Quiz_Marks: str
    Final_Marks: str

    def to_dict(self):
        return asdict(self)
