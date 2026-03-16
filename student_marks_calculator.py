print("===== Student Marks Calculator =====")

student_name = input("Enter student name: ")

subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))
subject4 = float(input("Enter marks of Subject 4: "))
subject5 = float(input("Enter marks of Subject 5: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

print("\n===== Result =====")
print("Student Name:", student_name)
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)