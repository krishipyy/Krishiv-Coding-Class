# Accepting integer input from the user
x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))
z = int(input("Enter value for z: "))

print("Before swapping :")
print("x =", x)
print("y =", y)
print("z =", z)


temp1 = z
z = y
y = x
x = temp1

print("After swapping :")
print("x =", x)
print("y =", y)
print("z =", z)