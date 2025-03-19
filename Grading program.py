student_scores = {
    "Harry": 81,
    "Ron":78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}


for value in student_scores:
    score = student_scores[value]
    if 91 <= score <= 100:
        student_grades[value] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[value] = "Exceeds Expectation"
    elif 71 <= score <= 80:
        student_grades[value] = "Acceptable"
    elif 0 <= score <= 70:
        student_grades[value] = "Fail"

print(student_scores)
print(student_grades)