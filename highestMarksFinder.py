student_marks = [2, 5, 3, 9, 23, 54, 12, 98]

highest = 0

for i in range(1, len(student_marks) + 1):
    if student_marks[i - 1] > highest:
        highest = student_marks[i + 1]

print(f"highest marks are {highest}")
