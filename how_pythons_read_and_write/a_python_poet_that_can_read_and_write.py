import random

with open("numbers.txt", "w") as numbers:
    for counts in range(20):
        numbers.write(str(random.randint(-100, 100)) + "\n")

with open("numbers.txt", "r") as numbers, \
    open("even.txt", "w") as even, \
    open("odd.txt", "w") as odd:

    for line in numbers:
        number = int(line.strip())
        if number % 2 == 0:
            even.write(str(number) + "\n")  
        else:
            odd.write(str(number) + "\n")    