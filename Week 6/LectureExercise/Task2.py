names = set()

while True:
    name = input("Give me a name: ")

    if name == "":
        for name in names:
            print(name)
        break
    elif name in names:
        print("Name exists")
    else:
        print("New name")
        names.add(name)
