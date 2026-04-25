import random

with open("numbers.txt", "w") as numbers:
    for counts in range(20):
        numbers.write(str(random.randint(-100, 100)) + "\n")
with open("even.txt", "w") as even:
    even.write("")

with open("odd.txt", "w") as odd:
    odd.write("")

with open("numbers.txt", "r") as numbers:
    for line in numbers:
        number = int(line.strip())
        if number % 2 == 0:
            #The number is even..
            with open("even.txt", "a") as even:
                even.write(str(number) + "\n")  
        elif number & 2 == 1:
            #The number is odd..
            with open("odd.txt", "a") as odd:
                odd.write(str(number) + "\n")    