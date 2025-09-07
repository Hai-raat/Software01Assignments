numbers = []

while True:
    input_str = input("Enter a number (or press enter to quit): ")
    if input_str == "":
        break
    numbers.append(int(input_str))

numbers.sort(reverse=True)

print("The five greatest numbers sorted in descending order are:", numbers[:5])