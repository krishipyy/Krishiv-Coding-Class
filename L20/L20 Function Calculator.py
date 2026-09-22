def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

try:
    a = float(input("Enter a number= "))
    b = float(input("Enter another number= "))

    choice = input("Enter the operation you want to perform (eg. +(1), -(2), *(3), /(4)): ")

    if choice == '1':
        print("The sum of ",a,"and",b,"is:",add(a,b))
    elif choice == '2':
        print("The difference of ",a,"and",b,"is:",subtract(a,b))
    elif choice == '3':
        print("The product of ",a,"and",b,"is:",multiply(a,b))
    elif choice == '4':
        print("The quotient of ",a,"and",b,"is:",divide(a,b))
    else:
        print("Invalid input, please enter a valid operation.")

except ValueError as ve:
    print("Exception value error:", ve)

except ZeroDivisionError as zde:
    print("Exception zero division error:", zde)
    