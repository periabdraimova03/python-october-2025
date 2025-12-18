# if you spent $100 and more you get 10% discount 
# if you spent $200 and more you get 15% discount
# if you spent $300 and more you get 20% discount

discount = 0
def calculate_tax(price):
    tax = price * 0.1
    return tax 

def apply_discount(price, discount_percentage):
    discount = price * (discount_percentage/100)
    return discount
price = float(input("Enter the price: "))
tax = calculate_tax(price)

if price >= 100 and price < 200:
    discount = apply_discount(price, 10)
elif price >= 200 and price < 300:
    discount = apply_discount(price, 15)
elif price >= 300:    
    discount = apply_discount(price, 20)

total_price = price + tax - discount

print(total_price)