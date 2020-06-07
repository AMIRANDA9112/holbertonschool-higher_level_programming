#!/usr/bin/python3
"""This module return a sorted list"""


class MyList(list):
    """
        class list
        """

    def print_sorted(self):
        """

                :return: sorted list
                """
        print(sorted(self))
