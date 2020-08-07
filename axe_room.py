import random 
from pip._vendor.colorama import Fore, Back, Style
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
*        MISS        *
*                    *
*                    *
*                    *
*        OOOOO       *
*                    *
*       ( ˘︹˘ )     *
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
*     （っ＾▿＾）    *
*                    *
*                    *
**********************
"""


    if welcome == 'goldenwizard':
        print(x)
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
        message = input("Throw your axe at the target? Enter 'yes' or 'no'. If you enter something different it will probably break. So don't. :D ")

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
        
        elif target > 4 and message == 'yes':
            axe_total -= 1
            print()
            print('You Missed the target!')
            print()
            print('***************************')
            print()
            print()
            print(d)
            print()
            print('Total Targets Hit')
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
        
        elif message == 'no':
            print()
            print('What are you scared?')
            print()
    else:
        print('*****************************************************')
        print()
        print('YOU WON THE GAME!!!!')
        print()
        print('Here is your Golden Axe! Use this Golden Axe to continue through the maze!')
        print()
<<<<<<< HEAD
        print('Your code for Room 2 is: ' + Fore.YELLOW + 'goldenaxe')
=======
        print('Your code for Room 2 is: goldenaxe')
>>>>>>> b4429ef2cfc96c83c17a7024da40b76626579586
        print()
        print(Fore.WHITE + '*****************************************************')

axe_room()


