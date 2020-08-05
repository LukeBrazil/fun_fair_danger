## Welcome lines

def welcome():
    print('''
Welcome to the FunFair! 
You are on an adventure in a world of magic and danger. Keep your wits about you.
Upon entering each room you will need to find a secret code. Don’t forget it; you will need to exit the FunFair at the end. 
Good luck, don’t forget your snacks water and fairy dust
''')
    

welcome()

### Enter room function

### Wizard room function

def wizard_room(): 
    print('''
You have entered a dimly lit room. A wizened figure sits in a corner clad in silver robes. She beckons you over to her chair.
''')

    

def main():
    wizard_room()
    game_on = False
    ask_question = 'N'
    while ask_question != 'Y'.lower():
        ask_question = input('"May I ask you some questions? As a warning, you will not exit this room until you speak with me. (Y or N)"\n')
    if ask_question != 'Y'.lower():
        game_on = False
    else:
        game_on = True
    while game_on == True:
        name = input('"Tell me your name my dear"\n')
        birth_year = int(input('"And what is your birth year?"\n'))
        love_wealth_happiness = input('"Very interesting. There is a lot to tell you but we don\'t have much time. Would you like to learn about love, money, or happiness?"\n')
        if love_wealth_happiness == 'love':
        elif love_wealth_happiness == ''



main()