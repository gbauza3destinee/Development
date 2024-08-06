#### if 0 <= num < 1:
    ##print("I am between 0 and 1")

'''
You have been assigned the task of creating a sales tax calculator for an e-commerce company. Write a Python function called calculate_final_price that takes the price of a product and the sales tax rate, and return the final price including tax.
The price should be a positive number, and the tax rate should be between 0 and 1 (exclusive).
 If either of them are outside of the valid range, raise a custom ValueError with an appropriate error message.
Now, test your implementation by asking the user to input a product price and sales tax rate,
 and call your function. Catch any potential ValueError raised by the function. '''


def calculate_final_price(price, sales_tax):
    ## price should be a positive number
    if price < 0: 
        print("Price should be positive")
    
    try :
        final_price = sales_tax + price 
        if sales_tax < 0 or sales_tax > 1 : 
            raise ValueError
    except ValueError as e:
    ## if outside range
    #  raise custom ValueError with error message
        print(f"Sales tax should be between 0 and 1:  {e}")
    else: 
        return final_price
 
price = input("Enter your price : ")
tax = input("Enter your tax")
final_price = calculate_final_price(float(price), float(tax))
print(final_price)



