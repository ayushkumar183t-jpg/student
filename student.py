# 1. Creates a dictionary where student names are keys and their marks are values
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# 2. Asks the user to input a student's name
name_input = input("Enter the student's name: ")

# 3 & 4. Retrieves and displays the marks, or handles missing names
if name_input in student_marks:
    print(f"{name_input}'s marks: {student_marks[name_input]}")
else:
    print("Student not found.")