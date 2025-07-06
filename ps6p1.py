def comp_ext_price(qty,unit_price):
    ext_price = qty * unit_price

    if ext_price > 100000.00:
        disc_amt = ext_price * 0.10
    else:
        disc_amt = 0

    disc_ext_price = ext_price - disc_amt

    return disc_ext_price

total_ext_price = 0

response = input("Do you want to start this program (Yes or No)?")

while(response == 'Yes'):
    qty = int(input("Enter quantity:"))
    unit_price = float(input("Enter unit price:"))
    ext_price = comp_ext_price(qty,unit_price)
    print("Extended price: $%.2f"% ext_price)
    print("Unit price: $%.2f"% unit_price)
    print("Quantity: ", qty)
    total_ext_price = total_ext_price + ext_price
    response =  input("Do you want to continue with this program (Yes or No)?")

print("Total extended price: $%.2f"% total_ext_price)