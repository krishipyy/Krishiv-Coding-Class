o = input("Enter the type of vehicle you want to customize\n1. Car\n2. Bike  : ")
if o == "1":
    print("What is your car type?")
    print("1. SUV, \n2. Offroader")
    i = input("Enter your choice(1 or 2): ")

    if i == "1":
        print("You have chosen SUV")
    else:
        print("You have chosen Offroader")
else:
    print("What is your bike type?")
    print("1. Sports Bikem \n2. Offroader")
    p = input("Enter your choice(1 or 2): ")
    
    if p == "1":
        print("You have chosen Sports Bike")
    else:
        print("You have chosen Offroader")
