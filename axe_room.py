

def axe_room():
    print()
    print('*******************************')
    print()
    print('Welcome to the Axe throwing game! Do you have what it takes?')
    print()
    print()
    welcome = input('Please Enter the Key from Room 1: ')
    print()
    print()
    axe_total = 7
    target_hit = 0
    if welcome.lower() == 'key':
        game_on = True
    elif welcome.lower() != 'key':
        axe_room()
        game_on == True
    while game_on == True and target_hit < 5:
        print('Three targets appear!')
        print()
        target = input('Throw axe at target? Enter yes or no. If you enter anything differntely the program will probably break. So dont. :D   ')

        if target.lower() == 'yes' or 'no':
            target_hit += 1
            axe_total -= 1
            print()
            print('You hit the target!')
            print()
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
        
            if target_hit == 3:
                print('*****************************************************')
                print()
                print('YOU WON THE GAME!!!!')
                print()
                print('Here is your Golden Axe! Use this Golden Axe to continue through the maze!')
                print()
                print('Your code for Room 2 is: GoldenAxe')
                print()
                print('*****************************************************')
                break
                

axe_room()

# import random


# def axethrow():
#     print('Three targets appear!')
#     target = int(input('Throw your axe at Target 1? Target 2? or Target 3?'))
#     if target == 1:
#         print('You missed!')
#         axe_total - 1
#     elif target == 2:
#         print('Target hit!')
#         axe_total - 1
#         target_hit + 1
#     elif target == 3:
#         axe_total - 1
#         print('Wow you suck!')

# def end_game():
#     print("Congrats you have completed this challenge! Now time for a riddle...")
#     print()
        


        # if target == 1:
        #     print('You missed!')
        #     axe_total -= 1
        #     print("Total Axes Remaining!: ")
        #     print(axe_total)
        #     print('Total Targets Hit!: ')
        #     print(target_hit)
        # elif target == 2:
        #     print('Target hit!')
        #     axe_total -= 1
        #     target_hit += 1
        #     print(axe_total)
        #     print('Total Targets Hit!: ')
        #     print(target_hit)
        # elif target == 3:
        #     axe_total -= 1
        #     print('Wow you suck!')    
        #     print("Total Axes Remaining!: ")
        #     print(axe_total)
        #     print('Total Targets Hit!: ')
        #     print(target_hit)