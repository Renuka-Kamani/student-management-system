# utils.py
def grade(score):
    try:
        score = float(score)
    except:
        score = 0
    pct = score / 400 * 100
    if pct >= 85: return 'A'
    if pct >= 70: return 'B'
    if pct >= 50: return 'C'
    return 'D'

def validate_student(data: dict):
    # Example validations
    if not data.get("Roll_No"): return False, "Missing Roll_No"
    try:
        att = float(data.get("Attendance_%",0))
        if att < 0 or att > 100: return False, "Invalid attendance"
    except: return False, "Attendance must be number"
    for f in ["Mid1_Marks","Mid2_Marks","Quiz_Marks","Final_Marks"]:
        try:
            if data[f]:
                val = float(data[f])
                if val < 0 or val > 100: return False, f"Invalid {f}"
        except: return False, f"{f} must be number"
    return True, "OK"