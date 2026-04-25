import random

with open("numbers.txt", "w") as file:
    for numbers in range(20):
        file.write(str(random.randint(-100, 100)) + "\n")