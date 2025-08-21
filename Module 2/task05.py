pound_per_talent = 20
lots_per_pound = 32
grams_per_lot= 13.3
talents = float(input("what is the number of talents? "))
pounds = float(input("what is the number of pounds? "))
lots = float(input("what is the number of lots? "))
total_grams = ((talents * pound_per_talent + pounds) * lots_per_pound + lots) * grams_per_lot
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f"The total mass is {kilograms} kilograms and {grams:.2f} grams.")