#!/usr/bin/env python

# this is used by other code in the module, namely the pdf generator.

def BinarySearch(itm_list, itm):
    '''
    Typical binary search algorithm for finding an item in a python list.
    @ params: list of items, desired item
    @ return: True when item is located, False otherwise
    '''
    first = 0
    last = len(itm_list)-1
    found = False
    while (first <= last and found == False):
        mid = (first + last)//2
        if (itm_list[mid] == itm): found = True
        else:
            if (itm < itm_list[mid]): last = mid -1
            else:                     first = mid+1


    return found
