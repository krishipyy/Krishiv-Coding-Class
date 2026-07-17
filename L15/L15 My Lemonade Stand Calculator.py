#part 1 : Define a function with no arguments to greet the customer
def greet_customer():
    print("Welcome to the Lemonade Stand!")
    print("Fresh Lemonade, made just for you. ")

#part 2 : Call the greet_customer function
greet_customer()
print()

#part 3: Ask for the price per cup and the number of cups sold
price_per_cup = float(input("What is the price per cup of lemonade? $"))
cups_sold = int(input("How many cups of lemonade did you sell? "))

#part 4:Define a function that takes arugments and returns the total cost
def calculate_total_cost(price, cups):
    total_cost = price * cups
    return total_cost

#part 5: Call calculate_total_cost function and store the result in a variable
total_cost = calculate_total_cost(price_per_cup, cups_sold)

#part  6:Use a built in function tto round the total, then print it
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
print()

#part 7: Ask how much money the customer paid
money_paid = float(input("How much money did the customer pay? "))

#part 8 : Define a function that takes arguments and returns the change due
def calculate_change(money, total):
    change = money - total
    return change

#part 9: Call calculate_change and store the value is it returns
change_due = calculate_change(money_paid, rounded_total)
rounded_change_due = round(change_due, 2)

#part 10: Define a function that returns a thank you message based on cup sold
def thank_you_message(cups):
    if cups >=5:
        return "Wow,big order! Thank you for your business!"
    else:
        return "THanks for stopping by the stand!"
    
#part 11: Call the thank_you_message function and print the result
closing_message = thank_you_message(cups_sold)
print()

#part 12:Print the final lemonade stand receipt
print()
print("==== LEMONADE STAND RECEIPT ====")
print("Price per cup: ", price_per_cup)
print("Cups sold: ", cups_sold)
print("Total cost: ", rounded_total)
print("Money paid: ", money_paid) 
print("Change due: ", rounded_change_due)
print(closing_message)
print("================================")