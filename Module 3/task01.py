limit = 42

length = int(input("Enter the length of the zander (cm): "))

if length < 42:
        print(f"Release the fish back into the lake. It is {limit - length} cm below the size limit.")
else:
        print("The Zander meets the size. You can keep it.")