#!/usr/bin/env python

# modules
import numpy as np

# home brew modules
from WarHammer.Dice import D

def GetAttributes(race):
    '''
    This function randomly rolls characteristics, and determines other main stats like 
    fate, resilliance, extra points, and movement. Also, wounds and encumberence.
    a tuple of two formats are returned, one to be used for generating pdfs, and the 
    second for text display.
    @ params: race
    @ returns: tuple of the two different formatted data.
    '''
    # need 5 tables for the ability scores, one for each race option
    # make a dictionary with races as keys.
    # the dictionary stores the ab score rudrics that races rolls
    # the arrays in the are the modifiers to the 2d10 roll
    # which are in order of [WS, BS, S, T, I, AG, Dex, Int, WP, Fel, Fate, Resilience, Extra Points, Movement]

    characteristics = ['WS', 'BS', 'S', 'T', 'I', 'AG', 'Dex', 'Int', 'WP', 'Fel']
    if race.endswith("Elf"): race = "Elf"
    hail_marys = ['Fate', 'Resilience', 'Extra Points', 'Movement']
    options = { "Human":    np.ones(10)*20,
                "Halfling": np.array([10, 30, 10, 20, 20, 20, 30, 20, 30, 30]),
                "Dwarf":    np.array([30, 20, 20, 30, 20, 10, 30, 20, 40, 10]),
                "Elf":      np.array([30, 30, 20, 20, 40, 30, 30, 30, 30, 20]) }
    # Fate, Resilience, Extra Points, Movement
    afterWounds = { "Human":    np.array([2, 1, 3, 4]),
                    "Halfling": np.array([0, 2, 3, 3]),
                    "Dwarf":    np.array([0, 2, 2, 3]),
                    "Elf":      np.array([0, 0, 2, 5]) }
    your_AB_scores = {}
    absNums = {}
    count = 0
    for mod in options[race]:
        r1 = D(10)
        r2 = D(10)
        absNums[characteristics[count]] = r1+r2+mod
        your_AB_scores[characteristics[count]] = "2d10 + mod = %2d + %2d + %2d = %2d"%(r1, r2, mod, absNums[characteristics[count]])
        count += 1

    # calculate wounds and encum
    SB = int(absNums['S']/10)
    TB = int(absNums['T']/10)
    WPB = int(absNums['WP']/10)
    if race == 'Halfling': absNums['Wounds'] = 2*TB+WPB
    else:                  absNums['Wounds'] = SB+2*TB+WPB
    absNums['Enc'] = SB+TB
    your_AB_scores['Wounds'] = "SB + 2*TB + WPB = %d + %d + %d = %2d" %(SB, (2*TB), WPB, absNums['Wounds'])
    your_AB_scores['Enc'] = "SB + TB = %d + %d = %2d" %(SB, (TB), absNums['Enc'])

    count = 0
    for lif in afterWounds[race]:
        your_AB_scores[hail_marys[count]] = str(lif)
        absNums[hail_marys[count]] = str(lif)
        count += 1
    
    return (your_AB_scores, absNums)
    
