#Assigning Different Variables 
name="Penguin"
age=15
is_student=True
weight=38.5

#Printing Different variables and their data types
print("Original:")
print("Name :",name)
print("Data type of name is ", type(name))

print("Age :",age)
print("Data type of age is ", type(age))

print("Is Student :",is_student)
print("Data type of is_student is ", type(is_student))

print("Weight :",weight)
print("Data type of weight is ", type(weight))

print()
print()

#Type casting to convert the datatypes of variables
print("After Typecasting......")
age=str(age)
print("Age after typecasting:"+age)
print("Data type of age is", type(age))

weight=int(weight)
print("Weight after typecasting:",weight)
print("Data type of weight is", type(weight))