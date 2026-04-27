highest_grade = 5
top_student = "No student in file."

try:
    with open("student_grades.txt", "r") as file:
        for line in file:
            student_name, grade = line.strip().split(",")
            try:
                grade = float(grade)
            except ValueError:
                print(f"Error: Invalid grade for student {student_name}.")
                continue
            if grade < highest_grade:
                highest_grade = grade
                top_student = student_name
except FileNotFoundError:
    print("Error: File not found.")

print(f"Top Student: {top_student} with a grade of {highest_grade}")