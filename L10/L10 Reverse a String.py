w = input("Enter any word: ")
rev = ""

for i in w:
    rev = i + rev

print(f"The reverse of the word {w} is: {rev}")