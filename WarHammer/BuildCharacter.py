#!/usr/bin/env python

# modules

# my modules
from WarHammer.GenerateText import GenerateText
from WarHammer.GeneratePDF import GeneratePDF
from WarHammer.GetCareerData import GetCareerData
from WarHammer.GetAttributes import GetAttributes
from WarHammer.GetClass import GetClass
from WarHammer.GetClassTrappings import GetClassTrappings
from WarHammer.GetJob import GetJob
from WarHammer.GetMoney import GetMoney
from WarHammer.GetPhysicalFeatures import GetPhysicalFeatures
from WarHammer.GetRace import GetRace
from WarHammer.GetRaceSkills import GetRaceSkills
from WarHammer.GetRaceTalents import GetRaceTalents

def main():
    '''
    This macro runs all the modules to make a completely random wh character
    '''
    # roll race
    race = GetRace()

    # get job & data
    job = GetJob(race)
    careerpath = GetCareerData(*job)

    # get attributes
    attributes = GetAttributes(race)
    
    # get race skills & talents
    race_skills = GetRaceSkills(race)
    race_talents = GetRaceTalents(race)

    # get class trappings
    traps = GetClassTrappings(job[0])
    stt = (race_skills, race_talents, traps)
    # all about the looks
    my_look = GetPhysicalFeatures(race)

    # get paid
    money = GetMoney(careerpath.status)

    # generate text
    filename = "beta_character.txt"
    GenerateText(race, *job, careerpath, attributes[0], *stt, *my_look, *money, filename)

    # generate pdf
    pdfname = 'beta_character.pdf'
    GeneratePDF(pdfname, race, *job, *my_look, attributes[1], race_talents, traps, careerpath, money)
    
if __name__ == '__main__':
    main()
