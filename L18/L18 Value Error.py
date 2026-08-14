try:
    num = int(input("Enter a number: "))
    print("The number enetered is:", num)

except ValueError as ve: #using valueError 
    print("Exception value error:", ve)

print("I am outside the try-except block") #always executed and displayed the message
print()