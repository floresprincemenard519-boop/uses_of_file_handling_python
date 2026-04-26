import random

with open("integers.txt", "w") as file:
    for numbers in range(20):
        num = random.randint(-100, 100)
        file.write(f"{num}\n")