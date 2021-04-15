import random
import re

random_words = [
    'lasagna',
    'bags',
    'love',
    'van',
    'backseat',
    'oak tree',
    'cherry',
    'summer',
    'winter',
    'boy',
    'girl',
]

sad_choice = ['troubling', 'boring', 'depressing', 'awful']
happy_choice = ['funny', 'fascinating', 'kinda cool']
other_choice = ['interesting', 'exotic', 'weird']

choices = sad_choice + happy_choice + other_choice

questions = [
    'What are you aiming for in life?: ',
    'If you had to choose between {}, {}, {}, what describes your love life right now?: ',
    'Would you like to... go out?: ',
    'Are you married?: ',
    'Are you in love?: ',
    'What music genre do you prefer?: ',
]

name = input('INSERT NAME: ')


print('Nice to meet you, {}'.format(name))

def question_maker():
    quest1 = input(questions[1].format(random.choice(choices), random.choice(choices), random.choice(choices)))
    if quest1 in sad_choice:
        print('sucks to be you')
    elif quest1 in happy_choice:
        print('huh, you really be vibin then')
    elif quest1 in other_choice:
        print('what the fuck')
    else:
        print('what an idiot, goodbye')
        return
    quest2 = input(questions[0])

question_maker()
