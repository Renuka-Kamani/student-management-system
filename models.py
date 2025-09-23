class Student:
    def __init__(self,attendence,name,roll_no,year,gender,age,mid_1,mid_2,final,quiz):
        self.roll_no=int(roll_no)
        self.name=str(name)
        self.age=int(age)
        self.year=int(year)
        self.gender=str(gender)
        self.mid_1=int(mid_1)
        self.mid_2=int(mid_2)
        self.final=float(final)
        self.quiz=float(quiz)
        self.attendence=float(attendence)
        self.checking()
    def checking(self):
        if self.roll_no<0:
            raise ValueError("give positive number")
        if self.attendence<=0 or self.attendence>=100:
            raise ValueError("give positive value for attendence")
    def to_dic(self):
        return{
        "Roll_No":self.roll_no,
        "Name":self.name,
        "Age":self.age,
        "Year":self.year,
        "Gender":self.gender,
        "Mid1_Marks":self.mid_1 if self.mid1 is not None else "",
        "Mid2_Marks":self.mid_2 if self.mid1 is not None else "",
        "Final_Marks":self.final if self.final is not None else "",
        "Quiz_Marks":self.quiz if self.quiz is not None else "",
        "Attendence_%":self.attendence
        }

        
    

