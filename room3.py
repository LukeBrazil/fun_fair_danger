# ROOM3 ROTTEN TOMATOES: Go ahead , pick your poison, a bucket full of rotten tomatoes at your disposal.
import random
def main():
   # welcome  = input()
    rotten_tomatoes = 3 # get 3 chances for a hit

    sarcasm_list =[
        "Well, aren't we just a ray of frigging sunshine.",
        "Do you know who I am?",
        "Jealousy is a disease… get well soon!",
        "How many times do I have to flush before you go away?",
        "Well, this day was a total waste of makeup.",
        "Back off! You’re standing in my aura.",
        "Whatever kind of look you were going for, you missed.",
        "Sarcasm is just one more service we offer.",
        "Aw, did I step on your poor little bitty ego?"
        ]
    play_again = ""

    while rotten_tomatoes >= -1:

        value = random.randint(0, len(sarcasm_list) -1) # shuffle sarcastic remarks with hit
        hit = random.randint(0,5)
    
        if rotten_tomatoes == 3:

            input("Hit enter to give it a rotten tomato strike!")
            if hit == 2:
                print("bingo!")
                break #win the game
            else:
                print(sarcasm_list[value])
                play_again = input("Would you like another chance?")
   
        if rotten_tomatoes == 2:
            rotten_tomatoes += 1
            input("Hit enter to give it a rotten tomato strike!")
            if hit == 1:
                print("ditto!")
                break #win the game
            else:
                print(sarcasm_list[value])
                play_again = input("Would you like another chance?")

            play_again == input("Think you can do better, how about another round?")
            print(sarcasm_list[value])

        if rotten_tomatoes == 1:
            rotten_tomatoes += 1
            input("Hit enter to give it a rotten tomato strike!")
            if hit == 0:
                print("dammit!")
                break #win the game

            else:
                print(sarcasm_list[value])
                play_again = input("Would you like another chance?")

            play_again == input("Last Chance?")
            print(sarcasm_list[value])

        rotten_tomatoes -= 1
    #print("bingo")

main()


