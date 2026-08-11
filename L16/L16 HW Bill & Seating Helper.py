def calculate_bill(bill_amount, tip_percentage):
    total = bill_amount * (1 + (tip_percentage / 100))
    return round(total, 2)

def calculate_seating(guests):
    """This recursive function calculates the total number of seating arrangements."""
    if guests == 0 or guests == 1:
        return 1
    else:
        return guests * calculate_seating(guests - 1)

entered_bill = float(input("Enter the initial bill amount: $"))
entered_tip = float(input("Enter the tip percentage: "))

final_amount = calculate_bill(entered_bill, entered_tip)

print()
print("Your total bill including tip is:")
print(final_amount)
print()

print("Function Documentation:")
print(calculate_seating.__doc__)
print()

entered_guests = int(input("Enter the number of guests for seating arrangements: "))
total_arrangements = calculate_seating(entered_guests)

print()
print(f"Total possible seating arrangements for {entered_guests} guests:")
print(total_arrangements)