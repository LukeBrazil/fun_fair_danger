# ROOM3 ROTTEN TOMATOES: Go ahead , pick your poison, a bucket full of rotten tomatoes at your disposal.
import random
def Tomato():

    rotten_tomatoes = 3 # get 3 chances for a hit (accumalator)
    game_running = True
    play_again = "y"
    ogre_conquered = False

    sarcasm_list =[
        "Well, aren't we just a ray of frigging sunshine.",
        "How many times do I have to flush before you go away?",
        "Well, this day was a total waste of makeup.",
        "Back off! You’re standing in my aura.",
        "Whatever kind of look you were going for, you missed.",
        "Sarcasm is just one more service we offer.",
        "Aw, did I step on your poor little bitty ego?"
    ]
    print("""
        Welcome to Room 3: 

        Yes, I know, an Ogre blocking the doorway.

        He won't move an inch, as if the Queen of England's Beefeaters.

        Try him, sneeze, laugh, have a pretend heart attacked!

        Please be advised, don't touch him, as Ogres can be very Cranky!

        Well, what are you waiting for?

        """)
#if expression == conditional always true
 #Statement
#else 
 #Statement
    question_one = input("Approach the Ogre? yes (y) or no (n)")
    if question_one == "y": 
        print("OK, you asked for it!")
    elif question_one == "n":
        print("Ogre approaching you! No limits set!")
    else:
        print("""
            Sorry! Only a small challenge!
        
            Bummer!

            No choice actually!

            Ogre still approaching!

            Grab a bucket Bimbo!
        """)

    while game_running and play_again == "y":
        
        value = random.randint(0, len(sarcasm_list) -1) # shuffle sarcastic remarks with hit
        hit = random.randint(0,100)
    
        if rotten_tomatoes == 3:
            input("Urgh! Hit enter, go for it, a rotten tomato strike!")
            if hit == 2:
                print("BINGO!")
                ogre_conquered = True
                break #game over
            else:
                print(sarcasm_list[value])
                play_again = input("Would you like another chance? yes (y) or no (n)")
   
        if rotten_tomatoes == 2:
            input("Get on with it! Hit enter! Any strickes this time?")
            if hit == 1:
                print("DITTO!")
                ogre_conquered = True
                break #game over
            else:
                print(sarcasm_list[value])
                play_again = input("Would you like another chance? yes (y) or no (n)")

        if rotten_tomatoes == 1:
            input("GO ON..., and hit enter again!")
            if hit == 0:
                print("DAMMIT, was the last one?")
                ogre_conquered = True
                break #game over
            else:
                print(sarcasm_list[value])
                print("You're all out of tomatoes!")
        
        rotten_tomatoes -= 1 # game change here
       
        if rotten_tomatoes == 0:
            play_again = ("yes (y) or no (n)")
            if play_again == "y":
                rotten_tomatoes = 3


    #print ("remember your key[room_3__key]")
    print("""
        With a healthy smile, muscles, bone and liver,
        You're - Off to the next maize-ing thither,
        Hopefully, not craving any liquor!

        Escaped the Dragons and muscle Engraving!
        Only to remember the slothtomato key-ring-er!

        You've been gifted a golden tomato, you will need this in the future!
        \nYour passcode to enter the next room is: slothtomato
        """)
room3entrance = input("What is the key from room 2?")
room3_passcode = room3entrance
if room3_passcode == "GoldenAxe":
    Tomato()


