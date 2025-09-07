import random
def roll_dice(sides):
    return random.randint(1, sides)

max_num = int(input("Enter the maximum number: "))
while True:
    result = roll_dice(max_num)
    print(result)
    if result == max_num:
        break