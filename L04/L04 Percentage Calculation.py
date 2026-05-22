# take marks as input from the user
print("Enter Marks Obtained in 5 subjects: ")

math = int(input("Maths: "))
science = int(input("Science: "))
english = int(input("English: "))
social = int(input("Social: "))
nepali = int(input("nepali: "))

# lets calculate the percentage of marks
sum = math + science + english + social + nepali
print("Sum of Maths, Science, English, Social and Nepali is", sum)


percentage = (sum / 500) * 100


print(f"percentage Marks= {percentage}%")
