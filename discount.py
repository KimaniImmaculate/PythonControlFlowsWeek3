def calculate_discount (price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#Ask for input from the user    
price=float(input("Enter the price: "))
discount_percent=float(input("Enter the discount percentage: "))

# Calculate the final price after discount
print("Final price after discount: ", calculate_discount(price, discount_percent))

#Or final_price = calculate_discount(price, discount_percent)
#final_price = calculate_discount(price, discount_percent)
