import random
import re

#DATABANK
one_three = {'color':['Blue', 'Gray', 'Black', 'Pale', 'Shading', 'Dark'],
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



questions = ['How well are you feeling right now?:\n1 -> 10',
'Name THREE of your all time favorite things:\n(spaced by only a coma)',
'What music genre do you prefer?\na)Pop  b)Jazz  c)Rock']
