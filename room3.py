# ROOM3 ROTTEN TOMATOES: Go ahead , pick your poison, a bucket full of rotten tomatoes at your disposal.
import random
from pip._vendor.colorama import Fore, Back, Style
def Tomato():
    rotten_tomatoes = 3 # get 3 chances for a hit (accumalator)
    game_running = True
    play_again = "y"
    ogre_conquered = False

    sarcasm_list=["\n-Well, aren't we just a ray of frigging sunshine.","\n-How many times do I have to flush before you go away?","\n-Well, this day was a total waste of makeup.","\n-Back off! You’re standing in my aura.","\n-Whatever kind of look you were going for, you missed", "\n-Sarcasm is just one more service we offer.","\n-Aw, did I step on your poor little bitty ego?"]

    print("""
        Welcome to Room 3: 

        Yes, I know, an Ogre blocking the doorway.

        He won't move an inch, as if the Queen of England's Beefeaters.

        Try him, sneeze, laugh, have a pretend heart attacked!

        Please be advised, don't touch him, as Ogres can be very Cranky!

        Well, what are you waiting for?

        """)

    question_one = input("\nApproach the Ogre? yes (y) or no (n) ")
    if question_one == "y": 
        print("\nOK, you asked for it!")
    elif question_one == "n":
        print("\nOgre approaching you! No limits set!")
    else:
        print("""
            Sorry! Only a small challenge!
            And Bummer! No choice actually!
            Ogre still approaching!

            \n\nGrab a bucket Bimbo!
        """)

    while game_running and play_again == "y":
        
        value = random.randint(0, len(sarcasm_list) -1) # shuffle sarcastic remarks with hit
        hit = random.randint(0,3)
    
        if rotten_tomatoes == 3:
            input("\n\nHit enter, go for a rotten tomato strike!")
            if  hit == 1:
                print("\nBINGO!")
                ogre_conquered = True
                break #game over
            else:
                print(sarcasm_list[value])
                play_again = input("\n\nWould you like another chance? yes (y) or no (n) ")
   
        if rotten_tomatoes == 1:
            input("\nGet on with it! Hit enter! Any strikes this time?")
            if hit == 1:
                print("\nDITTO!")
                ogre_conquered = True
                break #game over
            else:
                print(sarcasm_list[value])
                play_again = input("\n\nWould you like another chance? yes (y) or no (n) ")

        if rotten_tomatoes == 1:
            input("\nGO ON..., and hit enter again!")
            if hit == 1:
                print("\nDAMMIT, was the last one?")
                ogre_conquered = True
                break #game over
            else:
                print(sarcasm_list[value])
                print("""
                \nYou're all out of tomatoes!
                """)
        
        rotten_tomatoes -= 1 # game change here
       
        if rotten_tomatoes == 0:
            play_again = ("\nyes (y) or no (n)")
            if play_again == "y":
                rotten_tomatoes = 3

    print("""

        With a healthy smile, muscles, bones and liver,
        You're - Off to the next maize-ing thither,
        Hopefully, not craving any liquor!

        Escaped the Dragons and muscle engraving!
        Only to remember the goldentomato key-winger!

        You've been gifted a golden tomato, you will need this in the future!""")
    print("Your passcode to enter the next room is: " + Fore.YELLOW + "goldentomato")
room3entrance = input("\nEnter the key from room 2: ")
room3_passcode = room3entrance
if room3_passcode == "goldenaxe".lower():
    Tomato()


