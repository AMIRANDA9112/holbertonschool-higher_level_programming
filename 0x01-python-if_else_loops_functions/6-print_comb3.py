#!/usr/bin/python3
for n in range(0, 10):
    for i in range((n + 1), 10):
        if i != n:
            print("{:d}{:d}".format(n, i), end="")
            if n == 8 and i == 9:
                print("")
                break
            print(", ", end="")
