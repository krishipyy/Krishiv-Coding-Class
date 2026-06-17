#Take input from the user
n = int(input("Enter a number: "))

#initialize sum
sum = 0 

#total digit
power =len(str(n))

#find the sum of the cube of each digit
temp = n

while temp > 0:
    digit = temp % 10 #getting the reaminder of the divison
    sum = sum + digit ** power #calculate ea ch digit to the power of total digit and then add it to the sum
    temp = temp // 10 #floor division (the result is rounded down without decimal value)

#display the result
if n == sum:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number") 