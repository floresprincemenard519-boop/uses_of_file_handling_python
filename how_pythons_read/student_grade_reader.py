highest_grade = 5
top_student = "No student in file."

try:
    with open("student_grades.txt", "r") as file:
        for line in file:
            format_checker = line.strip().split(",")
            
            if len(format_checker) != 2:
                print(f"Incorrect format: {line.strip()}. Expected 'Name,Grade'")
                continue

            student_name, grade = format_checker 

            try:
                grade = float(grade)
            except ValueError:
                print(f"Error: Invalid grade for student {student_name}.")
                continue

            if grade < highest_grade:
                highest_grade = grade
                top_student = student_name

        print(f"Top Student: {top_student} with a grade of {highest_grade}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")

