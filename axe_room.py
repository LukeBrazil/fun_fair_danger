import random



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
        




def main():
    welcome = input('Welcome to the Axe throwing game! Do you have what it takes? Say yes or no...  ')
    axe_total = 4
    target_hit = 0
    game_won = False
    if welcome.lower() == 'yes':
        game_on = True
    elif welcome.lower() == 'no':
        main()
    while game_on == True:
        print('Three targets appear!')
        target = int(input('Throw your axe at Target 1? Target 2? or Target 3?'))
        print("Total Axes Remainig!: ")
        print(axe_total)
        print('Total Targets Hit!: ')
        print(target_hit)
        if target == 1:
            print('You missed!')
            axe_total -= 1
        elif target == 2:
            print('Target hit!')
            axe_total -= 1
            target_hit += 1
        elif target == 3:
            axe_total -= 1
            print('Wow you suck!')                
    if target_hit == 3:
        print('You won the game!')
        



main()