#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix != [[]]:
        for i in matrix:
            c = 1
            for n in i:
                if c == len(i):
                    print("{:d}".format(n), end='')
                else:
                    print("{:d}".format(n), end=' ')
                c += 1
            print(end="\n")
    else:
        print(end="\n")
