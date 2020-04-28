#!/usr/bin/env python

import random

def D(n):
    '''
    master die!
    @ params: an integer, n, s.t.  n > 1.
    @ return: a random integer in the set {1, ..., n}
    '''
    return random.randint(1, n)
