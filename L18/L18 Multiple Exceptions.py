try:
    num1, num2 = eval(input("Enter two numbers seperated by comma:"))
    result = num1 / num2

    #code = "if True print(Yes)"
    #exec(code)

    print("Result is:", result)
    #print("Result is :", testing) #this is name error 

except ZeroDivisionError:
    print("Division by zero is not allowed")

except SyntaxError:
    print("Syntax error")

except ValueError:
    print("Please enter numerical value")

except NameError as ex:
    print("The name error exception is:", ex)

except :
    print("Some error occured")

else:
    print("no exception or no error")

finally:
    print("I will execute no matter what happens ")
    
