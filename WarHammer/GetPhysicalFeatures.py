#!/usr/bin/env python

# modules
import importlib_resources
from contextlib import ExitStack
import atexit

# my modules
from WarHammer.OpenPickle import OpenPickle
from WarHammer.Dice import D

def GetPhysicalFeatures(race):
    '''
    Randomly selects age, height, eye color, hair color based on tables in rule book
    @ params: race
    @ returns: (age, height, eye color, hair color)
    '''
    file_manager = ExitStack()
    atexit.register(file_manager.close)
    
    ref_eye = importlib_resources.files('Pickles') / 'eye_table.pickle'
    path_eye = file_manager.enter_context(importlib_resources.as_file(ref_eye))

    eye_table = OpenPickle(path_eye) 
    eye_roll = D(10) + D(10)
    eye_color = ''
    for color, nums in eye_table[race].items():
        if eye_roll in nums:
            eye_color = color


    ref_hair = importlib_resources.files('Pickles') / 'hair_table.pickle'
    path_hair = file_manager.enter_context(importlib_resources.as_file(ref_hair))

    hair_table = OpenPickle(path_hair)
    hair_roll = D(10) + D(10)
    hair_color = ''
    for color, nums in hair_table[race].items():
        if hair_roll in nums:
            hair_color = color


    age = 0
    height = 0
    if race == 'Human':
        age = 15 + D(10)
        height = 2.54*(4*12 + 9 + sum([D(10) for i in range(0, 2)]))
    elif race == "Dwarf":
        age = 15 + sum([D(10) for i in range(0, 10)])
        height = 2.54*(4*12 + 3 + D(10))
    elif race == "Halfling":
        age = 15 + sum([D(10) for i in range(0, 5)])
        height = 2.54*(3*12 +1 + D(10))
    else:
        age = 30 + sum([D(10) for i in range(0, 10)])
        height = 2.54*(5*12+11+ D(10))

    return (age, height, eye_color, hair_color)
