def calculate_discount(price, discount_percent):
  if (discount_percent >= 20):
    price = price - (price * (discount_percent / 100))
  else:
    return price

price = float(input("Enter the original price of the item"))
discount_percent = float(input("Enter the discount percentage you were given"))

price_after_discount = calculate_discount(price, discount_percent)


print(f'final price after discount is: {price_after_discount})
