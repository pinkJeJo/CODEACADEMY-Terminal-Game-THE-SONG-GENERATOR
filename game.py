import random
import re

#DATABANK
zero_three = {'color':['Blue', 'Gray', 'Black', 'Pale', 'Shading', 'Dark'],
'time':['Winter', 'Yesterday', 'August', 'November', 'Night', 'Noon', 'Never'],
'adj':['The Worst', 'Sadly', 'Bad', 'Awful']}

four_seven = {'color':['Tinted', 'Blank', 'White', 'Teal'],
'time':['Autumn', 'Evening', 'Day', 'Spring', 'Today', 'Often'],
'adj':['Fine', 'Cool', 'Great', 'Comforting']}

eight_ten = {'color':['Yellow', 'Red', 'Bright', 'Pink', 'Sky'],
'time':['Summer', 'Spring', 'April', 'December', 'January', 'Day', 'Tomorroy', 'Today', 'Now'],
'adj':['Very Cool', 'Amazing', 'Great', 'Happy', 'Hype']}

things = []

places = ['USA', 'America', 'Alabama', 'Paris', 'Venice', 'Ipanema', 'The Coffe Shop', 'Backstreet', 'Your Apartment', 'Europe']

#SONG NAME TEMPLATES FOR REPLACING
jazz_temp = ['{color} {thing}',
'{color} {time}',
'{color} {place}',
'{time} In {place}',
'{adj} {thing}',
'The {person} In {place}'
]

pop_temp = ['Your {adj} {thing}',
'{color} {thing}',
'The {person} Of {time}',
'{thing} And {thing}',
]

rock_temp = ['Back in {color}',
'The {thing}',
'Road To {place}',
'{adj} Home {place}',
]

questions = ['How well are you feeling right now?\n0 -> 10  ==>',
'Name THREE of your all time favorite things:\n(spaced by only a coma)  ==>',
'What music genre do you prefer?\na)Pop  b)Jazz  c)Rock']

#INDIVIDUAL QUESTIONS FUNCTIONS
def quest1():
    ans1 = input(questions[0])
    if int(ans1) not in range(11):
        print('INCORRECT ANSWER')
    elif int(ans1) in range(4):
        return zero_three
    elif int(ans1) in range(4,8):
        return four_seven
    else:
        return eight_ten
#print(quest1())

def quest2():
    ans2 = input(questions[1])
    for thing in ans2.split(','):
        things.append(thing)
    return things
#print(quest2())

def quest3():
    ans3 = input(questions[2])
    if ans3 == 'a':
        return pop_temp
    elif ans3 == 'b':
        return jazz_temp
    elif ans3 == 'c':
        return rock_temp

#def question maker():
