#### if 0 <= num < 1:
    ##print("I am between 0 and 1")


def calculate_final_price(price, sales_tax):
    ## price should be a positive number
    if price < 0: 
        print("Price should be positive")
    
    try :
        final_price = sales_tax + price 
        if sales_tax < 0 or sales_tax > 1 : 
            raise ValueError
    except ValueError :
    ## if outside range
    #  raise custom ValueError with error message
        print("Sales tax should be between 0 and 1")
    else: 
        return final_price
 
price = input("Enter your price : ")
tax = input("Enter your tax")
final_price = calculate_final_price(float(price), float(tax))
print(final_price)



