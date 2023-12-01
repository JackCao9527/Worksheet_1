Tax = 0.13
Tom_size = 'L'
Helen_size = 'S'
Valdo_size = 'M'
price_for_small = float(input("please enter the price for Samll shirts: "))
price_for_medium = float(input("please enter the price for Medium shirts: "))
price_for_large = float(input("please enter the price for Large shirts: "))
print()
print("William store's prices: ")
print("=======================")
print("{:2} :  {:3}".format("Small", price_for_small))
print("{:2}:  {:2}".format("Medium", price_for_medium))
print("{:2} :  {:3}".format("Large", price_for_large))
print()
Qty_of_small_shirt = int(input("please enter the Qty for small shirt: "))
Qty_of_medium_shirt = int(input("please enter the Qty for medium shirt: "))
Qty_of_large_shirt = int(input("please enter the Qty for large shirt: "))
sub_total_for_samll = price_for_small * Qty_of_small_shirt
sub_total_for_medium = price_for_medium * Qty_of_medium_shirt
sub_total_for_large = price_for_large * Qty_of_large_shirt
sub_total_for_samll = round(sub_total_for_samll, 2)
sub_total_for_medium = round(sub_total_for_medium, 2)
sub_total_for_large = round(sub_total_for_large, 2)
tax_small = sub_total_for_samll * Tax
tax_medium = sub_total_for_medium * Tax
tax_large = sub_total_for_large * Tax
tax_small = round(tax_small, 2)
tax_medium = round(tax_medium, 2)
tax_large = round(tax_large, 2)
total_small = sub_total_for_samll + tax_small
total_medium = sub_total_for_medium + tax_medium
total_large = sub_total_for_large + tax_large
print()
print("{:10}  |  {:2}  |  {:2}  |  {:2}  |  {:2}  | {:5}  |  {:2}".format("Customer", "Size", "Price", "Qty", "Sub-total", "Tax", "Total"))
print("{:10}  |  {:4}  |  {:5}  |  {:3}  |  {:9}  | {:5}  |  {:4}".format("Helen", Helen_size, price_for_small, Qty_of_small_shirt, sub_total_for_samll, tax_small, total_small))
print("{:10}  |  {:4}  |  {:5}  |  {:3}  |  {:9}  | {:2}  |  {:4}".format("Tom", Tom_size, price_for_large, Qty_of_large_shirt, sub_total_for_large, tax_large, total_large))
print("{:10}  |  {:4}  |  {:5}  |  {:3}  |  {:9}  | {:5}  |  {:4}".format("Valdo", Valdo_size, price_for_medium, Qty_of_medium_shirt, sub_total_for_medium, tax_medium, total_medium))