def to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter gallons (negative to stop): "))
    if gallons < 0:
        break
    print(f"{gallons} gallons = {to_liters(gallons)} liters")