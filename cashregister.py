print("Enter price of the first item:")
price1 = int(input())

print("Enter price of the second item:")
price2 = int(input())

if (price1 < price2):
	priceafter = (50/100 * price1) + price2
if (price1 > price2):
	priceafter = (50/100 * price2) + price1

print("Does customer have a club card? (y/n):")
discount = input()
if (discount=="y"):
	discount = int(10/100 * priceafter)
if (discount=="n"):
	discount = 0

print("Enter tax rate:")
tax = float(input()) / 100

print("Base price = ", price1 + price2)
priceafter1=float(priceafter)
discount1=float(discount)

print("Price after discounts = ", priceafter - discount + (tax*priceafter))
