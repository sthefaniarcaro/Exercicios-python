# Description: Make a function that receives the price of a product and a discount rate, 
# and returns the final price after the discount.    

def discount(price, rate):
    disc = price * (rate/100)
    final_price = price - disc
    print(f'the discount is {disc} and the final price is {final_price}')

price = float(input('type a price: '))
rate = float(input('type a discount rate:'))

discount(price, rate)