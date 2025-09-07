import math
def unit_price(diameter, price):
    area = math.pi * (diameter / 200) ** 2
    return price / area

diameter_1 = float(input("Enter first diameter (cm): "))
price_1 = float(input("Enter first price (euro): "))
diameter_2 = float(input("Enter second diameter (cm): "))
price_2 = float(input("Enter second price (euro): "))
up1 = unit_price(diameter_1, price_1)
up2 = unit_price(diameter_2, price_2)
print(f"Pizza 1 unit price: {up1:.2f} euro/m²")
print(f"Pizza 2 unit price: {up2:.2f} euro/m²")
better = 1 if up1 < up2 else 2
print(f"Pizza {better} offers better value.")