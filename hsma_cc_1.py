#Team 4
# test
import pandas as pd

location = "security"
game_start = False
hr_complete = False
met_manager = False
obtain_id_form = False
talk_to_security = False
id_card = False

# Objects will be our nouns

# Functions will be our verbs
def get(object):

def examine(object):

def move(direction):

def look():

def speak(person, location):
    global talk_to_security, met_manager, hr_complete
    location = current_location
    if person in building.loc[location]['people'] and location == "security" and game_start == False :
        talk_to_security = True
        print("You talk to the security guard, he looks up from his phone and",
        "grunts you in the direction of the corridor")
        input("Do you want to move?")A
    elif (person in building.loc[location]['people'] and
     location == "security" and game_start == True and hr_complete == True):
    elif person in building.loc[location]['people'] and location == "corridor":
        
    elif person in building.loc[location]['people'] and location == "office":
        met_manager = True
    elif person in building.loc[location]['people'] and location == "hr" and obtain_id_form == True:
        hr_complete = True
    else:
        print("There is no one with that description present")


#list of objects

l_office = [
    "manager",
    "non-descript form",
    "dirty tea mug",
    "phone",
    "Dusty computer monitor"
    ]

l_corridor = [
    "Empty crisp packet",
    "Dust Bunny"
]
l_hr = [
    "Stapler",
    "Sign stating: No problems only opportunities",
    "HR specialist"
]
l_toilet = [
    "Toilet"
]
l_security = []
l_staffroom = ["cake"]
l_outside = ["open window"]
l_inventory = ["Job Offer", "Drivers License", "Utility Bill", "Reference"]

d_corridor = {
    "n" : "hr",
    "s" : "toilet",
    "e" : "security",
    "w" : "office"
}
d_hr ={
    "s": "corridor"
}
d_office = {
    "n" :"staff_room",
    "e" :"corridor"
}
d_toilet = {
    "n": "corridor",
    "s": "outside"
}

d_staffroom = {
    "s": "office",
    "n": "outside"
}

d_security = {
    "w": "corridor"
}
d_outside = {
    "s": "staff_room",
    "n": "toilet"
}

# List of rooms

building = pd.DataFrame({
    "room_name":["office","corridor", "hr", "toilet", "security", "staff_room","outside"],
    "items":[l_office,l_corridor,l_hr,l_toilet,l_security,l_staffroom, l_outside],
    "events":[d_office, d_corridor, d_hr, d_toilet, d_security, d_staffroom, d_outside],
    "people":["manager", "hr rep", "senior hr","","security guard", "",""]
})
building.set_index("room_name", inplace=True)

current_location = "security"
while talk_to_security == False:
    print(introduction),
    print(f"In front of you is a desk with {building['people'][4]}")

    

# goal
#staff_room|, HR,      Nil
#   ^    ,   ^       ,_____
#office>, corridor, <security
#_____,     v        ,_____
#nil,     Toilet,        nil

narrative = {
    "s1":"You are at the entrance of a dilapidated NHS office block. There is a door to the corridor.There is a security desk in front of you, manned by an agressive looking security guard.", # First time in security
    "s2":"You have returned to the security desk next to the hospital entrance. The security guard is sat at the desk still watching football on his phone", # Second time in security
    "c1":"You escape the distain of the scurity guard and enter a dreary corridor. A strong smell of bleach and overcooked peas hangs in the air. There are three doors off the corridor, one has a guardian near by", # First time in corridor
    "c2":"Back in the corridor, the bleached peas smell has gone, replaced with ",# Second time in corridor
    "o1":"You enter the office. The walls are gleaming white, clearly the hospital managment company has recently renewed the paint. On entering you receive a warm welcome from your manager, who welcomes you to the team. This is your first day working at St Hoots and Wotsits NHS Trust. Time for induction. Some time later you wake bleary eyed and you manager is still talking, now rather hoarsly. Your manager suggests that it is time to take a break. You are informed there is a delicious Taste the difference tripple chocolate fudge cake in the adjoining staff room and you should join the rest of the team for a slice and a cup of tea. you stand up and look around.", # First time in office
    "o2":"You enter the office. The Manager looks up saying, 'why are you back? You haven't been gone nearly long enough to have gotten your id badge yet!'.",# second time in office no achievements have tried the sr door
    "o3":"You enter the office. The manager looks up saying: 'Oh so you managed to run the HR gaunlet, congrats! Your predecessor never managed to return hence why we re-advertised the position.",# Third time in office has HR 
    "o4":"You enter the office. The manager looks up wide eyed 'Goodness, this has never happened before. You are the promised one who was fortold to be able to obtain an ID badge in one single day.",# fourth time in office has HR has ID badge
    "h1":"You enter HR. from some where in the mass of office cubicles you can hear a quiet sobbing. A Senior HR specialist is leant up against a desk chewing gum with a glazzed expression. ", # First time in hr
    "h2":"",# second time in ht
    "t1":"" # First time in toilet
}
#Security
#You are at the entrance of a dilapidated NHS office block. There is a door to the corridor.
#There is a security desk in front of you, manned by an agressive looking security guard.

#Corridor met_manager=False
#You are in a bland NHS corridor. There are four doors: Security, HR, Toilet, Office.
#The door to HR is blocked by an angry looking middle aged woman named Karen.
#The toilet is occupied.
#Look around - print(f"You can see {l_corridor}")

#Corridor met_manager=True
#You are in a bland NHS corridor. There are four doors: Security, HR, Toilet, Office.
#Look around - print(f"You can see {l_corridor}")

#Toilet
#You are in a toilet. The smell is horrendous. There is a door to the corridor and an open window.
#Look - print(f"You can see {l_toilet}")

#Office met_manager=False
#You are in a depressing NHS office. There are two doors: Corridor, Staff Room.
#The Staff Room door has a sign saying: ACCESS WITH ID CARD ONLY
#There is a very stressed manager sat at a desk eating cake.
#Look - print(f"You can see {l_office}")

#HR
#You are in an intimidating NHS HR department. There is a door to the corridor.
#Look - print(f"You can see {l_hr}")

#Staff Room
#You are in a dingy NHS staff room. There is a door to the office and an open window.
#Look - print(f"You can see {l_staffroom}")