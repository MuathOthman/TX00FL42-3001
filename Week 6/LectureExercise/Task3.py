airports = {}

while True:
    print("1. Enter a new airport.")
    print("2. Fetch information of an existing airport.")
    print("3. Quit")

    print()
    userChoose = input("Choose operation by typing 1-3: ")

    if userChoose == "1":
        print("New airport")
        print("------------")

        icao = input("Enter ICAO: ").lower()
        airport = input("Enter Airport name: ")

        airports[icao] = airport
        print("Added successfully")
    elif userChoose == "2":
        icao = input("Enter ICAO: ").lower()
        if icao in airports:
            print(f"ICAO: {icao.upper()} \nAIRPORT NAME: {airports[icao]}")
            print("--------------")
        else:
            print(f"There is now ICAO CODE with name {icao}. Please choose number 1")
    elif userChoose == "3":
        print("Quitting the program")
        break
    else:
        print("Wrong choise")