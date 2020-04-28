#!/usr/bin/env python

# my modules
from WarHammer.Dice import D

def GetMoney(status):
    ''' 
    You money is determined by your status (ie: Brass 4). 
    status is one of the CareerPath variables
    @ params: status
    @ returns: a tuple with (copper, silver, gold)
    '''
    cl, cn = status.split(' ')
    cn = int(cn)
    if (cl =="Brass"):
        return (sum([D(10) for i in range(0, 2*cn)]), 0, 0)
    elif (cl == 'Silver'):
        return (0, sum([D(10) for i in range(0, cn)]), 0)
    else:
        return (0, 0, cn)

