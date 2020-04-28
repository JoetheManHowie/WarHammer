#!/usr/bin/env python

# in future this class will be expanded to hold all the career path info for levelling up characters

class CareerPath():
    '''
    Designed to hold the required information for a career path 
    from the Warhammer Rule Book (i.e. 'Thief-taker', 'Silver 1', 
    list_of_career_skills, list_of_career_talents, list_of_career_trappings, 85)
    the lists, would actually be the different skills, talents, and trappings 
    listed on the page in the rule book.
    '''
    def __init__(self, name, status, skills, talents, trappings, page):
        self.name = name
        self.status = status
        self.skills = skills
        self.talents = talents
        self.trappings = trappings
        self.page = page


    def __repr__(self):
        return "On page "+ str(self.page)+"\n"+self.name+"--"+self.status


