def square_and_cube_generator(file_name):
    with open(file_name, "r") as file, \
         open("double.txt", "w") as squared_number, \
         open("triple.txt", "w") as cubed_number:
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                squared_number.write(f"{number ** 2}\n")
            elif number % 2 == 1:
                cubed_number.write(f"{number ** 3}\n")

square_and_cube_generator("integers.txt")