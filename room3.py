# ROOM3 ROTTEN TOMATOES: Go ahead , pick your poison, a bucket full of rotten tomatoes at your disposal.
import random
def main():

    rotten_tomatoes = 3 # get 3 chances for a hit (accumalator)
    game_running = True
    play_again = "y"
    troll_conquered = False

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
        Welcome to Room 3. 

        Yes, I know, a troll blocking the doorway.

        He won't move an inch, as if the Queen of England's Beefeaters.

        Try him, sneeze, laugh, have a pretend heart attacked!

        Only advise, don't touch him, he can be a bit cranky!

        Well, what are you waiting for, go on in!

        """)

    question_one = input("Approach the troll? yes (y) or no (n) ")
    if question_one == "y": 
        print("OK, you asked for it!")
    elif question_one == "n": 
        print("Troll approaching you")
        print("""
            Sorry!
        
            Bummer!

            No choice actually!

            Troll still approaching!

            Grab a bucket Bimbo!
        """)

    else: 
        print()

    while game_running and play_again == "y":
        
        value = random.randint(0, len(sarcasm_list) -1) # shuffle sarcastic remarks with hit
        hit = random.randint(0,100)
    
        if rotten_tomatoes == 3:
            input("Hit enter, go for it, a rotten tomato strike!")
            if hit == 2:
                print("bingo!")
                troll_conquered = True
                break #win the game
            else:
                print(sarcasm_list[value])
                play_again = input("Would you like another chance?")
   
        if rotten_tomatoes == 2:
            input("come on! any strickes this time?")
            if hit == 1:
                print("ditto!")
                troll_conquered = True
                break #win the game
            else:
                print(sarcasm_list[value])
                play_again = input("Would you like another chance? yes (y) or no (n)")

        if rotten_tomatoes == 1:
            input("go on, and hit enter!")
            if hit == 0:
                print("dammit!")
                troll_conquered = True
                break #win the game
            else:
                print(sarcasm_list[value])
                print("You ran out of tomatoes!")
        
        rotten_tomatoes -= 1 # game change here
       
        if rotten_tomatoes == 0:
            play_again = ("yes (y) or no (n)")
            if play_again == "y":
                rotten_tomatoes = 3



    print("Off to the next maize")

main()


