w = input("Do you have any medical conditions? (Y/N) ")
n = int(input("Enter your attendance number: "))

if w.upper() == "Y":
    print("You are eligible to take the exam")
else:
    if n >= 75:
        print("You are eligible to take the exam")
    else:
        print("You are not eligible to take the exam") 