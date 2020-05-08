#!/usr/bin/python3
def search_replace(my_list, search, replace,):
    """

    :type my_list: index on list
    """
    for i in my_list:
        if my_list[i] == search:
            my_list[i] = replace
            return my_list
