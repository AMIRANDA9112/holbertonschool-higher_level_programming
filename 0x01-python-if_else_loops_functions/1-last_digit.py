#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    ld = ((number * -1) % 10)
    ld = ld * -1
else:
    ld = (number % 10)
if ld > 5:
    print("Last digit of {:d} is {:d} ".format(number, ld) +
          "and is greater than 5")
elif ld < 6:
    if ld == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, ld))
    else:
        print("Last digit of {:d} is {:d} ".format(number, ld) +
              "and is less than 6 and not 0")
