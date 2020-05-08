#!/usr/bin/python3
def search_replace(my_list, search, replace,):
    """

    :type my_list: index on list
    """
    for i in my_list:
        if my_list[i] == search:
            la_list = my_list.copy()
            la_list[i] = replace
            return la_list


