# Part 1: Define a function with no arguments to greet the customer
def greet_customer():
    print("Welcome to Creative Corner Art Supplies!")
    print("Fuel your imagination with our quality materials.")

# Part 2: Call the greet_customer function
greet_customer()
print()

# Part 3: Ask for the price per item and the number of items sold
price_per_item = float(input("What is the price per art supply item? $"))
items_sold = int(input("How many items did the customer purchase? "))

# Part 4: Define a function that takes arguments and returns the total cost
def calculate_total_cost(price, quantity):
    total_cost = price * quantity
    return total_cost

# Part 5: Call calculate_total_cost function and store the result in a variable
total_cost = calculate_total_cost(price_per_item, items_sold)

# Part 6: Use a built-in function to round the total, then print it
rounded_total = round(total_cost, 2)
print("Total Cost:", rounded_total)
print()

# Part 7: Ask how much money the customer paid
money_paid = float(input("How much money did the customer pay? "))

# Part 8: Define a function that takes arguments and returns the change due
def calculate_change(money, total):
    change = money - total
    return change

# Part 9: Call calculate_change and store the value it returns
change_due = calculate_change(money_paid, rounded_total)
rounded_change_due = round(change_due, 2)

# Part 10: Define a function that returns a thank you message based on items sold
def thank_you_message(quantity):
    if quantity >= 5:
        return "Wow, what an art haul! Thank you for supporting our shop!"
    else:
        return "Thanks for stopping by Creative Corner! Happy creating!"
    
# Part 11: Call the thank_you_message function and store the result
closing_message = thank_you_message(items_sold)
print()

# Part 12: Print the final art supplies store receipt
print("==== CREATIVE CORNER RECEIPT ====")
print("Price per item: ", price_per_item)
print("Items sold: ", items_sold)
print("Total cost: ", rounded_total)
print("Money paid: ", money_paid) 
print("Change due: ", rounded_change_due)
print(closing_message)
print("=================================")