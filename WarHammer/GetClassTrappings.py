#!/usr/bin/env python

# my modules
from WarHammer.Dice import D

def GetClassTrappings(clas):
    '''
    In addition to the career trappings, your class gives you some trappings
    this function returns a list of your class trappings
    @ params: class
    @ returns: list of class trappings
    '''
    traps = {'ACADEMICS': ('Clothing', 'Dagger', 'Pouch',
                           'Sling Bag', 'Writing Kit', str(D(10)) +' sheets of Parchment'),
             'BURGHERS':  ('Cloak', 'Clothing', 'Dagger',
                           'Hat', 'Pouch', 'Sling Bag', 'Lunch'),
             'COURTIERS': ('Dagger', 'Fine Clothing',
                           'Pouch', 'Tweezers', 'Ear Pick', 'Comb'),
             'PEASANTS':  ('Cloak', 'Clothing', 'Dagger',
                           'Pouch', 'Sling Bag', 'Rations (1 day)'),
             'RANGERS':   ('Cloak', 'Clothing', 'Dagger',
                           'Pouch', 'Backpack', 'Tinderbox', 'Blanket', 'Rations (1 day)'),
             'RIVERFOLK': ('Cloak', 'Clothing', 'Dagger',
                           'Pouch', 'Sling Bag', 'Flask of Spirits'),
             'ROGUES':    ('Clothing', 'Dagger', 'Pouch',
                           'Sling Bag', '2 Candles', str(D(10))+' Matches', 'Hood or Mask'),
             'WARRIORS':  ('Clothing', 'Hand Weapon', 'Dagger', 'Pouch') }
    return traps[clas]
