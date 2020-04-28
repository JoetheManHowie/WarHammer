#!/usr/bin/env python

# my modules
from WarHammer.OpenPickle import OpenPickle

def GetClass(job):
    '''
    Looks up the class of a given career
    @ params: career (ie: 'Seaman')
    @ returns: the class of that career (ie: RIVERFOLK)
    '''
    cc = OpenPickle("Pickles/classes_table.pickle")
    return cc[job]
