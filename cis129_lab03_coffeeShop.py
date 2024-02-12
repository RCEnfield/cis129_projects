#cis129_lab03_coffeeShop.py
"""Coffee shop receipt program"""

print("""***************************************
My Coffee and Muffin Shop""")

#prompt number of coffees bought
num_coffee = int(input("Number of coffees bought? "))

#prompt number of teas bought
num_tea = int(input("Number of teas bought? "))

#prompt number of muffins bought
num_muffin = int(input("Number of muffins bought? "))

#prompt number of croissants bought
num_croissant = int(input("Number of croissants bought? "))

print("""***************************************\n
***************************************
My Coffee and Muffin Shop Receipt""")

#calculations for purchase totals
total_coffee = num_coffee * 5.00
total_tea = num_tea * 4.00
total_muffin = num_muffin * 4.00
total_croissant = num_croissant * 5.00
total_tax = (total_coffee + total_tea + total_muffin + total_croissant) * 0.06
total_all = total_coffee + total_tea + total_muffin + total_croissant + total_tax

print(num_coffee, 'Coffee at $5 each: $', total_coffee)
print(num_tea, 'Tea at $4 each: $', total_tea)
print(num_muffin, 'Muffins at $4 each: $', total_muffin)
print(num_croissant, 'Croissants at $5 each: $', total_croissant)
print('6% tax: $', total_tax)
print("""---------
Total: $""", total_all)
print("""***************************************""")

#Thank you for your purchase and use of our receipt program!
