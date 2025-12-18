import csv, os
from file_handler import load_students, BASE_DIR
from utils import grade

def generate_report():
    students = load_students()
    totals = []
    for s in students:
        total = sum([float(s[f]) if s[f] else 0 for f in ['Mid1_Marks','Mid2_Marks','Quiz_Marks','Final_Marks']])
        totals.append((s,total))
    print(f"Total students: {len(totals)}")
    for s,t in totals:
        print(s["Roll_No"], s["Name"], t, grade(t))
    report_file = os.path.join(BASE_DIR, "report.csv")
    with open(report_file,'w',newline='',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(["Roll_No","Name","Total","Grade"])
        for s,t in totals:
            w.writerow([s["Roll_No"],s["Name"],t,grade(t)])
    print("Report saved:", report_file)
