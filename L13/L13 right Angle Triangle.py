print("Half Pyramid Pattern of Stars(*):")
i = int(input("Enter the number of rows: "))


for j in range(i): #outer loop to handle number of rows
    for k in range(j + 1): #inner loop to handle number of columns
        print("* ", end="") #display result 

    print()