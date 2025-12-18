from file_handler import load_students

def search_student():
    students = load_students()
    q = input("Search by Roll or Name: ").strip()
    results = [s for s in students if s["Roll_No"] == q or q.lower() in s["Name"].lower()]
    if results:
        for s in results:
            print(s)
    else:
        print("No student found")
