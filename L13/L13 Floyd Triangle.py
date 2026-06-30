rows = int(input("Please enter the total number of rows : "))
number = 1 #initialise by 1

print("Floyd's triangle ")

for i in range(rows): #representing rows
    for j in range(i + 1): #representing columns
        print(number, end='  ')
        number = number + 1

    print()
    