class SquareAndCubeGenerator:
    def __init__(self, file_name):
        self.file_name = file_name

    def square_and_cube_generator(self):
        try:
            with open(self.file_name, "r") as file, \
                open("double.txt", "w") as squared_number, \
                open("triple.txt", "w") as cubed_number:

                for line in file:
                    number = line.strip()
                    
                    if not number:
                        continue
                    try:
                        number = int(number)
                        if number % 2 == 0:
                            squared_number.write(f"{number ** 2}\n")
                        elif number % 2 == 1:
                            cubed_number.write(f"{number ** 3}\n")
                    except ValueError:
                        print(f"Invalid number: {line.strip()}")

        except FileNotFoundError:
            print(f"File not found: {self.file_name}")
        except Exception as error:
            print(f"An error occurred: {error}")
