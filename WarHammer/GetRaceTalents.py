#!/usr/bin/env python

# modules
import importlib_resources
import atexit
from contextlib import ExitStack

# my modules
from WarHammer.OpenPickle import OpenPickle
from WarHammer.Dice import D

def GetRaceTalents(race):
    '''
    Each race gets each of the talents listed (and with an 'or' pick one)
    Additionally, any random talents are rolled for you.
    @ params: race
    @ returns: list of race talents
    '''
    race_talents = {"Human":    ['Doomed', 'Savvy or Suave', '3 Random Talents'],
                    "Dwarf":    ['Magic Resistance', 'Night Vision', 'Read/Write or Relentless',
                                 'Resolute or Strong-minded', 'Sturdy'],
                    "Halfling": ['Acute Sense (Taste)', 'Night Vision', 'Resistance (Chaos)',
                                 'Small', '2 Random Talents'],
                   "High Elf": ['Acute Sense (Sight)', 'Coolheaded or Savvy', 'Night Vision',
                                'Second Sight or Sixth Sense', 'Read/Write'],
                   "Wood Elf": ['Acute Sense (Sight)', 'Hardy or Second Sight', 'Night Vision',
                                'Read/Write or Very Resilient', 'Rover'] }
    my_talents = race_talents[race]
    is_rand = my_talents[-1].split()
    # check for random talents
    if is_rand[0] in ('2', '3'):
        my_talents = my_talents[:-1]
        num_rand_talents = int(is_rand[0])
        file_manager = ExitStack()
        atexit.register(file_manager.close)
        ref = importlib_resources.files('Pickles') / 'RandTalent_table.pickle'
        path_rand_tal = file_manager.enter_context(importlib_resources.as_file(ref))
        rand_talent_table = OpenPickle(path_rand_tal)
        i = 0
        while i < num_rand_talents:
            roll = D(100)
            rolled_talent = ''
            for talent, nums in rand_talent_table.items():
                if roll in nums:
                    rolled_talent = talent
                
            
            if rolled_talent in my_talents: continue
            my_talents.append(rolled_talent)
            i += 1
        
    
    return my_talents
