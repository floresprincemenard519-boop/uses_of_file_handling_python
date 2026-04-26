with open("student_grades.txt", "r") as file:
    for line in file:
        student_name, grade = line.strip().split(",")
        print(f"Student: {student_name}, Grade: {grade}")