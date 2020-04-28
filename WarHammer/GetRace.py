#!/usr/bin/env python

# my modules
from WarHammer.Dice import D

def GetRace():
    '''
    Randomly selects a race based table in the rule book.
    @ returns: string of the roled race
    '''
    roll = D(100)
    if roll < 91:
        return "Human"
    elif roll > 90 and roll < 95:
        return "Halfling"
    elif roll > 95 and roll < 99:
        return "Dwarf"
    elif roll == 99:
        return "High Elf"
    else:
        return "Wood Elf"

    return 0
