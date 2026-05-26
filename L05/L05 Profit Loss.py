costprice = int(input("Enter the cost price: "))
sellingprice = int(input("Enter the selling price: "))

if sellingprice > costprice:
    print("Profit")

    pt= sellingprice - costprice
    print(pt)

else :
    print("No profit")
