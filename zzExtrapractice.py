#Converting scores to grades

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for name in student_scores:
    if student_scores[name] <= 70:
        student_grades[name] = "Fail"
    elif 71 <= student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    elif 81 <= student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectations"
    else:
        student_grades[name] = "Outstanding"



