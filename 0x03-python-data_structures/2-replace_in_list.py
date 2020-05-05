#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        continue
    if idx < 0 or idx >= i:
        return None
    else:
        my_list[idx] = element
        return my_list