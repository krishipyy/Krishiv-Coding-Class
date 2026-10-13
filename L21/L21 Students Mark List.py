print("empty list:")
empty_list = []
print(empty_list)
print()

student_marks = [85, 90, 78, 92, 88, 76, 95]
print("Original Student Marks List:")
print(student_marks)
print()

attendance_flags = [1, 0, 1] * 3
print("Repeating Attendance Flags List:")
print(attendance_flags)
print()

print("Marks list in reverse order:")
reversed_marks = student_marks[::-1]
print(reversed_marks)
print()

total_sum = 0
for mark in student_marks:
    total_sum = total_sum + mark

average_mark = total_sum / len(student_marks)

print("sum=", total_sum)
print("average =", average_mark)
print()

student_marks.sort()
print("sorted array in ascending order: ", student_marks)
print()

print("Smallest element is:", student_marks[0])
print()

print("Largest element is:", student_marks[-1])