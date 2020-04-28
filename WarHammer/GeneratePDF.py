#!/usr/bin/env python

# modules
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import white, black 

# my modules
from WarHammer.CareerPath import CareerPath
from WarHammer.BinarySearch import BinarySearch


class armor():
    def __init__(self, loc, enc, ap, qual):
        self.loc = loc
        self.enc = enc
        self.qual = qual
    
        
def GeneratePDF(pdf, race, Class, career, age, height, eye, hair, ABS, talent, traps, careerpath, cash):

    c = canvas.Canvas(pdf)
    curry = 820
    c.setFont("Courier", 20)
    c.drawCentredString(300, curry, 'Warhammer Character Sheet')
    c.setFont("Courier", 14)
    form = c.acroForm
    ### Top of page 1
    # character name
    curry -= 30
    c.drawString(10, curry, 'Name:')
    curry -= 5
    next_insert(form, 50, curry, 200, 20, "")
    # species
    curry += 5
    c.drawString(250, curry, 'Species:')
    curry -= 5
    next_insert(form, 320, curry, 100, 20, race)
    # class
    curry += 5
    c.drawString(420, curry, 'Class:') 
    curry -= 5
    next_insert(form, 470, curry, 100, 20, Class) 
    
    #career
    curry -=30
    c.drawString(10, curry, 'Career:')   
    curry -= 5
    next_insert(form, 70, curry, 180, 20, career)
    # career level
    curry += 5
    c.drawString(260, curry, 'Career Level:')   
    curry -= 5
    next_insert(form, 370, curry, 200, 20, "See page "+str(careerpath.page))
    
    # career path
    curry -=30
    c.drawString(10, curry, 'Career Path:')   
    curry -= 5
    next_insert(form, 110, curry, 280, 20, careerpath.name)
    # status
    curry += 5
    c.drawString(410, curry, 'Status:')   
    curry -= 5
    next_insert(form, 470, curry, 100, 20, careerpath.status)
    
    # Age
    curry -=30
    c.drawString(10, curry, 'Age:')   
    curry -= 5
    next_insert(form, 50, curry, 60, 20, str(age))
    # height
    curry += 5
    c.drawString(115, curry, 'Height:')   
    curry -= 5
    next_insert(form, 180, curry, 100, 20, str(round(height, 0))+" cm")
    # Hair
    curry += 5
    c.drawString(285, curry, 'Hair:')   
    curry -= 5
    next_insert(form, 330, curry, 100, 20, hair)
    # eyes
    curry += 5
    c.drawString(440, curry, 'Eye:')   
    curry -= 5
    next_insert(form, 475, curry, 95, 20, eye)
    
    ## Characterisitcs
    curry -= 20
    c.drawString(60, curry, 'Characterisitcs')   
    c.drawString(290, curry, 'Fate')
    c.drawString(360, curry, 'Resilience')
    c.drawString(485, curry, 'Experience')   
    ## abs
    c.setFont("Courier", 12)
    curry -= 20
    ab = ('WS', 'BS', 'S', 'T', 'I', 'AG', 'Dex', 'Int', 'WP', 'Fel')
    spacing = (13, 39, 67, 92, 117, 139, 160, 186, 215, 235)
    for i in range(0, len(ab)):
        c.drawString(spacing[i], curry, ab[i])   
    
    curry -= 22
    i = 10
    j=0
    while i < 240:
        next_insert(form, i, curry, 22, 20, str(int(ABS[ab[j]])))
        i +=25
        j +=1
    
    curry -= 20
    i = 10
    while i < 240:
        next_insert(form, i, curry, 22, 20,'')
        i +=25
    
    curry -= 20
    i = 10
    j = 0
    while i < 240:
        next_insert(form, i, curry, 22, 20, str(int(ABS[ab[j]])))
        i +=25
        j += 1
    
    # Fate
    curry += 60
    c.drawString(270, curry, 'Fate:')
    curry -= 5
    next_insert(form, 330, curry, 15, 20, str(int(ABS['Fate'])))
    curry -= 15
    c.drawString(270, curry, 'Fortune:')
    curry -= 5
    next_insert(form, 330, curry, 15, 20, str(int(ABS['Fate'])))
    # Resilience
    curry += 25
    c.drawString(355, curry, 'Resilience:')
    curry -= 5
    next_insert(form, 440, curry, 15, 20, str(int(ABS['Resilience'])))
    curry -= 15
    c.drawString(355, curry, 'Resolve:')
    curry -= 5
    next_insert(form, 440, curry, 15, 20, str(int(ABS['Resilience'])))
    # Experience
    curry += 25
    c.drawString(465, curry, 'Current:')
    curry -= 5
    next_insert(form, 530, curry, 50, 20, '')
    curry -= 15
    c.drawString(465, curry, 'Total:')
    curry -= 5
    next_insert(form, 510, curry, 70, 20, '')
    # Movement
    curry -= 10
    c.setFont('Courier', 14)
    c.drawString(360, curry, 'Movement:')
    c.setFont('Courier', 12)
    curry -= 20
    c.drawString(270, curry, 'Movement:')
    curry -=5
    next_insert(form, 350, curry, 22, 20, str(int(ABS['Movement'])))
    curry += 5
    c.drawString(385, curry, 'Walk:')
    curry -=5
    next_insert(form, 435, curry, 22, 20, str(2*int(ABS['Movement'])))
    curry += 5
    c.drawString(470, curry, 'Run:')
    curry -=5
    next_insert(form, 510, curry, 22, 20, str(4*int(ABS['Movement'])))
    
    curry -=15
    c.drawString(190, curry, 'Extra Points:')
    curry -=5
    next_insert(form, 290, curry, 15, 20, str(int(ABS['Extra Points'])))
    curry += 5
    curry -=15
    #curry -=30
    
    # Basic Skills & Advanced Skills
    tbs = 15
    c.setFont("Courier", 14)
    c.drawString(80, curry, 'Basic Skills')
    c.drawString(320, curry, 'Grouped & Advanced Skills')
    curry -= tbs
    c.setFont("Courier", 12)
    c.drawString(10, curry, 'Name             | Charac. | Adv')
    c.drawString(310, curry, 'Name             | Charac. | Adv')
    #
    sl = (('Art              | Dex     |', 'Dex'),
          ('Athletics        | Ag      |', 'AG'),
          ('Bribery          | Fel     |', 'Fel'),
          ('Charm            | Fel     |', 'Fel'),
          ('Charm Animal     | WP      |', 'WP'),
          ('Climb            | S       |', 'S'),
          ('Consume Alcohol  | T       |', 'T'),
          ('Cool             | WP      |', 'WP'),
          ('Dodge            | Ag      |', 'AG'),
          ('Drive            | Ag      |', 'AG'),
          ('Endurance        | T       |', 'T'),
          ('Entertain        | Fel     |', 'Fel'),
          ('Gamble           | Int     |', 'Int'),
          ('Gossip           | Fel     |', 'Fel'),
          ('Haggle           | Fel     |', 'Fel'),
          ('Intimidate       | S       |', 'S'),
          ('Intuition        | I       |', 'I'),
          ('Leadership       | Fel     |', 'Fel'),
          ('Melee (Basic)    | WS      |', 'WS'),
          ('Melee            | WS      |', 'WS'),
          ('Navigation       | I       |', 'I'),
          ('Outdoor Survival | Int     |', 'Int'),
          ('Perception       | I       |', 'I'),
          ('Ride             | Ag      |', 'AG'),
          ('Row              | S       |', 'S'),
          ('Stealth          | Ag      |', 'AG'))
    blank= '                 |         |'
    curry -=5 
    # race skills
    bas = []
    ass = []
    bs = 0
    all_sk = [s.split("|")[0].rstrip() for s,_ in sl]
    #print (all_sk)
    for skill in careerpath.skills:
        in_list = BinarySearch(all_sk, skill)
        if (in_list):
            bas.append(skill)
        else:
            ass.append(skill)
    
    #print(bas, ass)
    for i in range(0, len(all_sk)):
        sk, ab = sl[i]
        curry -= tbs
        c.drawString(10, curry, sk)
        c.drawString(310, curry, blank)
        curry -=5
        in_list = BinarySearch(bas, all_sk[i])
        if (in_list):
            next_insert(form, 180, curry, 22, 20, str(int(ABS[ab])))
            next_insert(form, 217, curry, 22, 20, '5')
        else:
            next_insert(form, 180, curry, 22, 20, str(int(ABS[ab])))
            next_insert(form, 217, curry, 22, 20, '')
            # advanced
        if len(ass) >0:
            next_insert(form, 310, curry, 120, 20, ass[0])
            next_insert(form, 442, curry, 35, 20, '')
            next_insert(form, 482, curry, 22, 20, '')
            next_insert(form, 517, curry, 22, 20, '5')
            ass = ass[1:]
        else:
            next_insert(form, 310, curry, 120, 20, '')
            next_insert(form, 442, curry, 35, 20, '')
            next_insert(form, 482, curry, 22, 20, '')
            next_insert(form, 517, curry, 22, 20, '')
            
        
    c.showPage()
    
    ## Page 2
    
    ## Talents
    c.setFont("Courier", 14)
    curry = 820
    c.drawString(150, curry, 'Talents')
    c.drawString(420, curry, 'Trappings')
    curry -= tbs
    c.setFont("Courier", 12)
    c.drawString(10, curry, 'Talent Name         | T. | Description')
    c.drawString(380, curry, 'Name                  | Enc')
    
    count = 0
    # career talents
    rtal = str(careerpath.talents)
    talent.append(rtal)
    for ta in talent:
        #print(ta)
        curry -= tbs*2
        next_insert(form, 10, curry, 150, 20, ta)
        next_insert(form, 165, curry, 22, 20, '')
        next_insert(form, 200, curry, 175, 20, '')
        count+=1
    curry +=tbs*2*count
    
    # pull out these item for later
    armour = ['Leather Breastplate',
              'Leather Jack',
              'Leather Jerkin',
              'Leather Leggings',
              'Mail Shirt']
    # location enc ap qualities
    a_stat = {'Leather Breastplate': ('Body', '2', '2', 'Weakpoints'),
              'Leather Jack': ('Arms, Body', '1', '1', ''),
              'Leather Jerkin': ('Body', '1', '1', ''),
              'Leather Leggings': ('Legs', '1', '1', ''),
              'Mail Shirt': ('Body', '2', '2', 'Flexible')}
    # group enc r/r damage qualities
    weapons = ['Axe',
               'Dagger',
               'Flail',
               'Knuckledusters',
               'Hand Weapon',
               'Hand Weapon (Boat Hook)',
               'Rapier',
               'Hand Weapon (Sword)',
               'Shield',
               'Weapon (Any Melee)' ]
    w_stat =  {'Axe': ['Basic', '1', 'Average', 'SL+SB+4', ''],
               'Dagger': ['Basic', '0', 'Varies', 'SL+SB+2', ''],
               'Flail': ['Flail', '1', 'Average', 'SL+SB+5', 'Distract, Wrap'],
               'Knuckledusters': ['Brawling', '0', 'Personal', 'SL+SB+2', ''],
               'Hand Weapon': ['Basic', '1', 'Average', 'SL+SB+4', ''],
               'Hand Weapon (Boat Hook)': ['Basic', '1', 'Average', 'SL+SB+4', ''],
               'Rapier': ['Fencing', '1', 'Long', 'SL+SB+4', 'Fast, Impale'],
               'Hand Weapon (Sword)': ['Basic', '1', 'Average', 'SL+SB+4', ''],
               'Shield': ['Basic', '1', 'Very Short', 'SL+SB+2', 'Shield 2, Defensive, Undamaging'],
               'Weapon (Any Melee)':['', '', '', '', ''] }
    
    # career trappings
    count2 = 0
    traps = list(traps)
    traps.extend(list(careerpath.trappings))
    traps.sort()
    any_a = []
    any_w = []
    while len(weapons) > 0:
        itm = weapons[0]
        in_weapons = BinarySearch(traps, itm)
        if in_weapons:
            traps.remove(itm)
            any_w.append(itm)
            
        weapons = weapons[1:]   
        
    while len(armour) > 0:
        itm = armour[0]
        in_armor = BinarySearch(traps, itm)
        if in_armor:
            traps.remove(itm)
            any_a.append(itm)
        armour = armour[1:]
        
        
    for itm in traps:
        curry -= tbs*2
        next_insert(form, 380, curry, 160, 20, itm)
        next_insert(form, 550, curry, 22, 20, '')
        count2 +=1
        
        
    pad = abs(count - count2)
    e = 0
    # special cases
    if (curry == 715 and pad*2*tbs): curry +=tbs*2
    else:                            curry +=tbs*2*pad
    
    if count > count2:
        curry -=2*tbs
        while e < pad:
            curry -=2*tbs
            next_insert(form, 380, curry, 160, 20, '')
            next_insert(form, 550, curry, 22, 20, '')
            e+=1
    elif count < count2:
        while e < pad:
            curry -=2*tbs
            next_insert(form, 10, curry, 150, 20, '')
            next_insert(form, 165, curry, 22, 20, '')
            next_insert(form, 200, curry, 175, 20, '')                
            e +=1
    e=max(count,count2)
    while e < 11:
        curry -=2*tbs
        next_insert(form, 10, curry, 150, 20, '')
        next_insert(form, 165, curry, 22, 20, '')
        next_insert(form, 200, curry, 175, 20, '')                
        next_insert(form, 380, curry, 160, 20, '')
        next_insert(form, 550, curry, 22, 20, '')
        e +=1
    
        
    # Ambitions
    c.setFont("Courier", 14)
    curry -= 15
    c.drawString(100, curry, 'Personal Ambitions')
    c.drawString(380, curry, 'Party Ambitions')
    curry -= 20
    L =['ST:', 'LT:']
    for g in L:
        c.drawString(10, curry, g)
        c.drawString(300, curry, g)
        curry -= 5
        next_insert(form, 40, curry, 250, 20, '')
        next_insert(form, 325, curry, 250, 20, '')
        curry -= 15
    
    # Armour
    c.drawString(250, curry, 'Armour')
    curry -= 20
    c.setFont('Courier', 12)
    c.drawString(10, curry, 'Name                 | Location | Enc | AP | Qualities')
    left = len(any_a)
    while len(any_a) != 0:
        curry -= 25
        key = any_a[0]
        values = a_stat[key]
        next_insert(form, 10, curry, 150, 20, key)
        next_insert(form, 177, curry, 55, 20, values[0])
        next_insert(form, 252, curry, 25, 20, values[1])
        next_insert(form, 290, curry, 30, 20, values[2])
        next_insert(form, 330, curry, 250, 20, values[3])
        any_a = any_a[1:]
    
    for i in range(left, 6):
        curry -= 25
        next_insert(form, 10, curry, 150, 20, '')
        next_insert(form, 177, curry, 55, 20, '')
        next_insert(form, 252, curry, 25, 20, '')
        next_insert(form, 290, curry, 30, 20, '')
        next_insert(form, 330, curry, 250, 20, '')
        
        
    ## body
    curry -=25
    c.drawString(10, curry, "Head: ")
    curry -=5
    next_insert(form, 44, curry, 22, 20, '')
    curry +=5
    c.drawString(68, curry, "| Left Arm: ")
    curry -=5
    next_insert(form, 147, curry, 22, 20, '')
    curry +=5
    c.drawString(171, curry, "| Right Arm: ")
    curry -=5
    next_insert(form, 258, curry, 22, 20, '')
    curry +=5
    c.drawString(285, curry, "| Body: ")
    curry -=5
    next_insert(form, 337, curry, 22, 20, '')
    curry +=5
    c.drawString(363, curry, "| Left Leg: ")
    curry -=5
    next_insert(form, 443, curry, 22, 20, '')
    curry +=5
    c.drawString(470, curry, "| Right Leg: ")
    curry -=5
    next_insert(form, 558, curry, 22, 20, '')
    curry -= 20
    curry +=5
    c.drawString(470, curry, "| Shield: ")
    curry -=5
    next_insert(form, 558, curry, 22, 20, '')

    c.drawString(250, curry, 'Weapons')
    curry -= 20
    c.setFont('Courier', 12)
    c.drawString(10, curry, 'Name                 | Group | Enc | R/R | Danage | Qualities')
    #print(any_w)
    left = len(any_w)
    while len(any_w) != 0:
        curry -= 25
        key = any_w[0]
        values = w_stat[key]
        next_insert(form, 10, curry, 150, 20, key)
        next_insert(form, 169, curry, 50, 20, values[0])
        next_insert(form, 233, curry, 25, 20, values[1])
        next_insert(form, 267, curry, 40, 20, values[2])
        next_insert(form, 313, curry, 60, 20, values[3])
        next_insert(form, 377, curry, 213, 20, values[4])
        any_w = any_w[1:]
    
    for i in range(left, 6):
        curry -= 25
        next_insert(form, 10, curry, 150, 20, '')
        next_insert(form, 169, curry, 50, 20, '')
        next_insert(form, 233, curry, 25, 20, '')
        next_insert(form, 267, curry, 40, 20, '')
        next_insert(form, 313, curry, 60, 20, '')
        next_insert(form, 377, curry, 213, 20, '')
        
    c.showPage()
    
    ## Page 3
    cash_d = ('| D:', '| SS:', '| GC:')
    space = ((70, 100), (130, 170), (200, 240))
    curry = 820
    c.setFont('Courier', 14)
    c.drawString(10, curry, 'Wealth:')
    c.setFont('Courier', 12)
    i = 0
    for a, b in space:
        c.drawString(a, curry, cash_d[i])
        curry -=5
        next_insert(form, b, curry, 25, 20, str(cash[i]))
        curry +=5
        i +=1

    c.setFont('Courier', 14)
    c.drawString(275, curry, '| Encumbrance: | Max:    | Total:')
    curry -=5
    next_insert(form, 455, curry, 25, 20, str(int(ABS['Enc'])))
    next_insert(form, 555, curry, 25, 20, '')
    curry -= 25
    
    # Wounds
    c.drawString(10, curry, 'Wounds:')
    c.setFont('Courier', 12)
    c.drawString(70, curry, '| Total:     | Current:     | Critical: ')
    curry -= 5
    next_insert(form, 132, curry, 25, 20, str(int(ABS['Wounds'])))
    next_insert(form, 242, curry, 25, 20, str(int(ABS['Wounds'])))
    next_insert(form, 355, curry, 25, 20, '0')
    curry -= 25
    c.setFont('Courier', 14)
    c.drawString(10, curry, 'Conditions:')
    curry -= 5
    next_insert(form, 110, curry, 470, 20, '')
    curry -= 25
    # Curruptions and Mutations
    c.drawString(10, curry, 'Insanities:     | Corruptions:     | Mutations: ')
    curry -= 5
    next_insert(form, 115, curry, 25, 20, '0')
    next_insert(form, 275, curry, 25, 20, '0')
    next_insert(form, 415, curry, 25, 20, '0')
    curry -= 15
    # Notes
    c.drawString(250, curry, 'NOTES')
    i = 0
    curry -=5
    while i < 35:
        curry -= 20
        next_insert(form, 10, curry, 570, 20, '')
        i +=1
    
    c.save()
        
        
def next_insert(form, xpos, ypos, wbox, hbox, val):                     
    form.textfield(value =val, x=xpos, y=ypos, borderStyle='inset',                 
                   borderColor=white, fillColor=white,                  
                   width=wbox, height = hbox, textColor=black) 
    
        
