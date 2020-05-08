#!/usr/bin/python3
def search_replace(my_list, search, replace,):
    """

    :type my_list: index on list
    """
    for i in my_list:
        if my_list[i] == search:
            lalist = my_list.copy()
            lalist[i] = replace
            return lalist
