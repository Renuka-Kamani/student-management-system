# sorting_filtering.py
from file_handler import load_students

def sort_students(field, reverse=False):
    students = load_students()
    return sorted(students, key=lambda s: s.get(field,""), reverse=reverse)

def filter_students(branch=None, year=None):
    students = load_students()
    if branch:
        students = [s for s in students if s["Branch"].lower() == branch.lower()]
    if year:
        students = [s for s in students if s["Year"] == year]
    return students