#Take input of a word
x = input("Enter any word or sentence: ")

#Take input of a character 
y = input("Enter the character you want to count: ")

i = 0
count = 0

#loop will find the occurence of character
while(i < len(x)):
    if(x[i] == y):
        count = count + 1

    i = i + 1


print(f"The total number {y} character has occured ={count} times")
