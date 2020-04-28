#!/usr/bin/env python

def GetRaceSkills(race):
    '''
    Each race picks 3 skills to give 5 advances, and 3 skills to give 3 advances
    Each race has a difference list of possible skills.
    @ params: race
    @ returns: list of skills.
    '''
    race_skills = { "Human":    ('Animal Care', 'Charm', 'Cool', 'Evaluate', 'Gossip', 'Haggle',
                                 'Language (Bretonnian)', 'Language (Wastelander)', 'Leadership',
                                 'Lore (Reikland)', 'Melee (Basic)', 'Ranged (Bow)'),
                    "Dwarf":    ('Consume Alcohol', 'Cool', 'Endurance', 'Entertain (Storytelling)',
                                 'Evaluate', 'Intimidate', 'Language (Khazalid)', 'Lore (Dwarfs)',
                                 'Lore (Geology)', 'Lore (Metallurgy)', 'Melee (Basic)', 'Trade (any one)'),
                    "Halfling": ('Charm', 'Consume Alcohol', 'Dodge', 'Gamble', 'Haggle',
                                 'Intuition', 'Language (Mootish)', 'Lore (Reikland)', 'Perception',
                                 'Sleight of Hand', 'Stealth (Any)', 'Trade (Cook)' ),
                    "High Elf": ('Cool', 'Entertain (Sing)', 'Evaluate', 'Language (Eltharin)',
                                 'Leadership', 'Melee (Basic)', 'Navigation', 'Perception',
                                 'Play (anyone)', 'Ranged (Bow)', 'Sail', 'Swim'),
                    "Wood Elf": ('Athletics', 'Climb', 'Endurance', 'Entertain (Sing)',
                                 'Intimidate', 'Language (Eltharin)', 'Melee (Basic)', 'Outdoor'
                                 'Survival', 'Perception', 'Ranged (Bow)', 'Stealth (Rural)', 'Track') }
    return race_skills[race]
