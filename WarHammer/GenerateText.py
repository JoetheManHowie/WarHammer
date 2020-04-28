#!/usr/bn/env python

# modules
import pandas as pd

def GenerateText(Race, myClass, myJob, career_data, attributes, race_skills, race_talents, traps, age, height, eye, hair, c, s, g, textfile):
    '''
    creates a text file with all the necessary info to make your character 
    (legacy code from the original 'Make_a_character.py' script)
    @ params: race, class, career, career_data, attributes, race_skills, race_talents, traps, physical feature, cash, textfile
    @ return: None
    creates a .txt file eplaining how to complete your character
    '''
    txt = open(textfile,'w')
    for args in (("RACE:", Race), ("CLASS:", myClass), ("CAREER:", myJob)):
        txt.write("{0:<10} {1:<10}\n".format(*args))
        
    txt.write("See page "+str(career_data.page)+ " for more details\n")
    txt.write(str(pd.DataFrame.from_dict(attributes, orient = 'index')))
    
    txt.write("\n\nSKILLS:\t(Pick three with 3 pts Advance, and three with 5 pts Advance):\n")
    [txt.write("\t%s\n" %sk) for sk in race_skills ]
    txt.write("FROM CAREER: (you get 40 advances between the eight, with a max of 10 in any one skill)\n")
    #[txt.write("\t%s\n" %sk) for sk in career_data.skills ]
    '''txt.write("Go to your Career Path and Spend 40 pts Advance on your starting skills \n\
    (Max 10pts per skill with these points) Note there is enough Advance \n\
    to put 5 pts in each skill in your starting class (which is required to level up)!\n")'''
    
    txt.write("TALENTS: (Humans & Halfling, Random Talents are rolled for you):\n")
    [txt.write("\t%s\n" %ta) for ta in race_talents ]
    txt.write("FROM CAREER: (pick ONE)\n")
    [txt.write("\t%s\n" %ta) for ta in career_data.talents ]
    txt.write("Note: if any doubles occurred, you may re-roll.\n\
    Go to your Career Path Take ONE talent from your starting career path.\n")
    
    
    txt.write("Physical Features:\n")
    for args in (("Age:", age), ("Height:", str(int(height))+" cm"), ("Eye Color:", eye), ("Hair Color:", hair)):
        txt.write("\t{0:<15} {1:<15}\n".format(*args))
        
    txt.write("\nTrappings: (You also get the trappings from your career)\n")
    [txt.write('\t%s\n' %itm) for itm in traps]
    
    [txt.write('\t%s\n' %itm) for itm in career_data.trappings]
    
    txt.write('You have: %d gold, %d silver, and %d copper\n' %(g, s, c))
    
    txt.close()
