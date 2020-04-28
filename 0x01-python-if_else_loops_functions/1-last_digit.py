#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    las = number % 10
else:
    las = number % -10

if las == 0:
    text = "and is 0"
elif las > 5:
    text = "and is greater than 5"
elif las < 6:
    text = "and is less than 6 and not 0"

print("Last digit of", number, "is", las, text)

