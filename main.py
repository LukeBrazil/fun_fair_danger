# from room_1
# from room2
# from room3
# from room4_finished

from intro import print_intro
from room_1 import run_fortune_teller
from room2 import axe_room
from room3 import Tomato
from room4_finished import room4
from ending import lol

def play():
    print_intro()
    run_fortune_teller()
    axe_room()
    Tomato()
    room4()
    play_again 

game_on = True
play_again = input('Play again? ')
while game_on == True:
    play()
if play_again == 'yes':
    play()
else:
    lol()
