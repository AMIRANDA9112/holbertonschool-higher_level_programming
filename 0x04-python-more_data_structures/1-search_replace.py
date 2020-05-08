#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """

    :param replace: new element
    :param search: element to replace
    :type my_list: index on list
    """
    la_list = my_list.copy()  # type: list
    for i in range(len(la_list)):
        if la_list[i] == search:
            la_list[i] = replace
    return la_list
