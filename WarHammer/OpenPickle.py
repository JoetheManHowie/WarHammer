#!/usr/bin/env python

# modules
from pickle import load

def OpenPickle(pickle_file):
    pickle_in = open(pickle_file, 'rb')
    my_dic = load(pickle_in)
    return my_dic
