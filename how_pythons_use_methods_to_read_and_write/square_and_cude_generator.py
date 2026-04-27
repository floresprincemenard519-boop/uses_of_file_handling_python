with open("integers.txt", "r") as file:
    with open("double.txt", "w") as squared_number:
        pass
    with open("triple.txt", "w") as cubed_number:
        pass
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            with open("double.txt", "a") as squared_number:
                squared_number.write(f"{number ** 2}\n")
        elif number % 2 == 1:
            with open("triple.txt", "a") as cubed_number:
                cubed_number.write(f"{number ** 3}\n")