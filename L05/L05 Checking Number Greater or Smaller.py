n = int(input("Enter a number: "))

if n <= 15 :
    print(f"{n} is smaller than or equal to 15")
    print("I'm in the if block")

else:
    print(f"{n} is greater than 15")
    print("I'm in the else block")

print("I'm not in the if block and I'm not in the else block")
