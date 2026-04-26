highest_grade = 0
top_student = ""

with open("student_grades.txt", "r") as file:
    for line in file:
        student_name, grade = line.strip().split(",")
        grade = float(grade)
        print(f"Student: {student_name}, Grade: {grade}")
        if grade > highest_grade:
            highest_grade = grade
            top_student = student_name

print(f"\nTop Student: {top_student} with a grade of {highest_grade}")