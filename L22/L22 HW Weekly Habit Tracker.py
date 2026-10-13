days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
habits = (1, 1, 0, 1, 1, 0, 1)

completed = 0
missed = 0

print("--- WEEKLY HABIT TRACKER ---")

for i in range(0, 7):
    if habits[i] == 1:
        print(days[i] + ": Done")
        completed = completed + 1
    else:
        print(days[i] + ": Missed")
        missed = missed + 1

print("----------------------------")
print("Total Completed:", completed)
print("Total Missed:", missed)

if completed > missed:
    print("Overall Status: Great job this week!")
else:
    print("Overall Status: Need to focus more next week!")