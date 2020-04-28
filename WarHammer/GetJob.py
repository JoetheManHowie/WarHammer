#!/usr/bin/env python

# modules
import importlib_resources
from contextlib import ExitStack
import atexit

# my modules
from WarHammer.Dice import D 
from WarHammer.OpenPickle import OpenPickle

def GetJob(race):
    '''
    need 5 tables of careers, one for each race
    there are Careers which are grouped in sets called Classes
    each races has a dictionary
    in that dic the career is the KEY and
    the VALUE is a list of numbers corresponding
    to the Career ex: human_careers = {..., 'Nun': [4, 5], ...}
    Then you can look up the Class in the Class dic 
    ex: human_classes = {'Academic': [..., 'Nun',...], ...}
    @ params: race
    @ returns: class, and career
    '''
    file_manager =ExitStack()
    atexit.register(file_manager.close)

    ref_career = importlib_resources.files('Pickles') / 'career_table.pickle'
    path_career = file_manager.enter_context(importlib_resources.as_file(ref_career))

    ref_class = importlib_resources.files('Pickles') / 'classes_table.pickle'
    path_class = file_manager.enter_context(importlib_resources.as_file(ref_class))

    master_map = OpenPickle(path_career)
    career_class = OpenPickle(path_class)
    # TIME TO ROLL
    roll = D(100)
    my_possible_careers = master_map[race]
    for career, nums in my_possible_careers.items():
        if roll in nums:
            return career_class[career], career


    return 0


