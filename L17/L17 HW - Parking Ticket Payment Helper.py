def calculate_change(paid, price):
    change = paid - price
    return change 

print("===== PARKING TICKET SYSTEM =====")

valid_zones = ['A', 'B', 'C', 'D']
zone_found = False

while not zone_found:
    code = input("Enter your parking zone code (A, B, C, or D): ").upper()
    for char in code:
        if char in valid_zones:
            print(f"Zone {char} verified successfully!")
            zone_found = True
            break
    if not zone_found:
        print("Invalid zone code, try again!\n")

ticket_price = 50
print(f"\nThe parking fee is {ticket_price} units.")
print("Accepted coins: 5, 10, 25, 50")
print()

total_inserted = 0 
coins_inserted = 0

while True:
    coin = int(input("Insert a coin (5, 10, 25, or 50): "))

    if coin != 5 and coin != 10 and coin != 25 and coin != 50:
        print("Invalid coin, try again!")
        print()
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}")
    print()

    if total_inserted >= ticket_price:
        print("Enough money inserted!")
        print()
        break

change_due = calculate_change(total_inserted, ticket_price)

print("Printing parking ticket...")

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units.")

print("\n===== PARKING TICKET SUMMARY =====")
print("Zone Code:", code)
print("Ticket Price:", ticket_price)
print("Coins Inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change_due)
print("==================================")
print("Thank you! Have a safe journey.")