#!/usr/bin/python3
for n in range(0, 10):
    for i in range(0, 10):
        if i == 9 and n == 9:
            print("{:d}{:d}".format(n, i), end="")
        else:
            print("{:d}{:d}, ".format(n, i), end="")
