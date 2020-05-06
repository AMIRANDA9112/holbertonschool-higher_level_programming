#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    la_list = my_list
    for i in la_list:
        continue
    if idx < 0 or idx >= i:
        return la_list
    else:
        la_list[idx] = element
        return la_list
