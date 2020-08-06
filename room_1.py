from helper import enter
from fortune_telling import fortune_topic



## Welcome lines
welcome = '''Welcome to the FunFair! 
You are on an adventure in a world of magic and danger. Keep your wits about you.
Upon entering each room you will need to find a secret code. Don’t forget it; you will need to exit the FunFair at the end. 
Good luck, don’t forget your snacks, water, and fairy dust. Presse enter to continue!'''

### Enter wizard room
wizard_room = "You have entered a dimly lit room. A wizened figure sits in a corner clad in silver robes. She beckons you over to her chair."
    
## main function
'''
Wizard room start
'''
def run_fortune_teller():
    enter(welcome)
    enter(wizard_room)
    game_on = False
    ask_question = 'N'
    while ask_question != 'Y'.lower():
        ask_question = enter('"May I ask you some questions? As a warning, you will not exit this room until you speak with me. (Y or N)"\n')
    if ask_question != 'Y'.lower():
        game_on = False
    else:
        game_on = True
    while game_on == True:
        name = enter('"Tell me your name my dear"\n')
        birth_year = int(enter('"And what is your birth year?"\n'))
        fortune_topic()



run_fortune_teller()
