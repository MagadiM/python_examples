'''
The purpose of this function is to calculate the total price of items based on the discount percentage provided. If the discount is below 20% the price will stand but if the discount is more than 20% then the discount is applied.
'''
def calculate_discount(price, discount):
    # using the try...except block to run the code and throw errors at the end
    try:
        price = float(price)
        discount = float(discount)

        if discount < 20:
            return price;
        else :
            finalPrice = price - (price * discount / 100)
            return finalPrice;
    except ValueError:
        return "Invalid input. Please add numerical numbers"

price = input("Enter the item's price: ")
discount = input("Enter discount percentage: ")

# Calculating total price and displaying the final price
totalPrice = calculate_discount(price, discount)
print(f"The total price is: {totalPrice}")