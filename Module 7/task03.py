airports = {}

while True:
    print("\nChoose an option:")
    print("1 = Enter new airport")
    print("2 = Fetch airport info")
    print("3 = Quit")
    choice = input("Your choice: ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport saved.")

    elif choice == "2":
        icao = input("Enter ICAO code: ").upper()
        if icao in airports:
            print(f"{icao} = {airports[icao]}")
        else:
            print("No airport found with that ICAO code.")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")