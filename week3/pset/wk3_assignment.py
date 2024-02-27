#week3 assignment

#declare discount base rate
discount_base_rate = 20

#function to calculate price
def calculate_discount(price, discount_percent):
    #check if discount applies
    if discount_percent >= discount_base_rate:
        final_price = price * (1 - discount_percent / 100)
        print(f'final price after discount is: , ${final_price:.2f}')

    else:
        print(f'original price without discount is: , ${price:.2f}')

#function to ask user for input
def get_price_and_discount():
    price = float(input('please, enter a price: '))
    discount_percent = float(input('please, enter a discount: '))
    return price, discount_percent

#call the functions directly
price, discount_percent = get_price_and_discount()
calculate_discount(price, discount_percent)
