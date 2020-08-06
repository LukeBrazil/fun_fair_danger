import random 

def axe_room():
    print('Welcome to the Axe Room Challenge. Do you have what it takes?')
    welcome = input('Please enter key from room 1: ')
    axe_total = 10
    target_hit = 0
    game_on = True
    d = """
**********************
*                    *
*                    *
*         MISS       *
*                    *
*                    *
*                    *
*        OOOOO       *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************
"""
    s = """
**********************
*                    *
*                    *
*         HIT        *
*                    *
*                    *
*                    *
*         XXX        *
*                    *
*                    *
*                    *
*                    *
*                    *
**********************
"""


    if welcome == 'key':
        pass

    while game_on == True and target_hit < 3:
        print()
        print('***************************')
        print()
        print('   Three targets appear!')
        print()
        print('***************************')
        print()
        print()

        target = random.randint(1, 6)
        message = input('Throw your axe at the target?')

        if target < 5 and message == 'yes':
            target_hit += 1
            axe_total -= 1
            print()
            print()
            print('You hit the target!')
            print()
            print(s)
            print('***************************')
            print()
            print('Total targets hit ')
            print()
            print(target_hit)
            print()
            print('Axes remaining')
            print()
            print(axe_total)
            print()
            print('***************************')
            print()
            print()
        
        elif target > 4:
            axe_total -= 1
            print()
            print('You Missed the target!')
            print()
            print('***************************')
            print()
            print('Total targets hit ')
            print()
            print(d)
            print()
            print(target_hit)
            print()
            print('Axes remaining')
            print()
            print(axe_total)
            print()
            print('***************************')
            print()
            print()
    else:
        print('*****************************************************')
        print()
        print('YOU WON THE GAME!!!!')
        print()
        print('Here is your Golden Axe! Use this Golden Axe to continue through the maze!')
        print()
        print('Your code for Room 2 is: GoldenAxe')
        print()
        print('*****************************************************')

axe_room()