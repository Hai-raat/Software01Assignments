def remove_odds(numbers):
    return [x for x in numbers if x % 2 == 0]

my_list = [9, 31, 7, 18, 13, 19]
new_list = remove_odds(my_list)
print(f"Original: {my_list}")
print(f"Even only: {new_list}")