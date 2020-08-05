def room4():
    print("""After a long and daunting journey through the Fun Fair Maze, you have entered the fourth and final room! \n You first notice the elegance of the room.\nThe white marble tiled floors are accented with gold and the walls are covered with rennaisannce styled paintings.\nIn the middle of the room, hangs a large diamond chandelier. \n After looking around, you guesstimate that this room is about 20x20 feet. \n \n Suddenly, beneath the chandelier a large troll dressed in garments and robes of royalty forms from the marble floors. The troll is holding some sort of angelic glowing orb. \n The troll exclaims; "I am Gorgish, King of the Fun Fair Maze! In order to exit the maze, you must give me the three items you've acquired from the former rooms. Then you must answer my riddle that only a true Fun Fair Maze champion would know. If you guess correctly, my orb will wisk you away to safety. Beware, you will only get three guesses to answer my riddle correctly""")
    
    room1_unlocked = input("What did you acquire from room 1? ")
    
    # The troll is asking if you brought the correct item from room1
    if room1_unlocked == "x":
        room1_unlocked == True
        print("Excellent")
        #The troll is asking if you brought the correct item from room2
        room2_unlocked = input("What did you acquire from room 2? ")
        if room2_unlocked == "y":
            room2_unlocked == True
            print("Excellent")
            #The troll is asking if you brought the correct item from room3
            room3_unlocked = input("What did you acquire from room 3? ")
            if room3_unlocked == "z":
                room3_unlocked == True
                print("Excellent! You have moved onto the final challange: The Fun Fair Maze Riddle.")
                #the troll is asking the final riddle
                final_riddle_answer = input("The Final Riddle is, geeofotefwfaoe. What is your answer? ")
                if final_riddle_answer == "a":
                    final_riddle_answer == True
                    print("""King Gorgish says; "You are correct! You may return to safety!" \nGorgish's orb glows bright white, the power of the orb pulls you into it. \nYou and the orb are now one! Beams of bright light radiate out of you.\nThe elegant room slowly fades to dark. Suddenly you are transported to the entrance of the maze.\nYou are champion of the Fun Fair Maze!""")
                else:
                    print("""Gorgish says; "Wrong!" The elegant room shrinks drastically. The room now appears to be 10x10 in size.\nYou are worried if you answer wrong two more times, you'll be smashed into oblivion.""")
                
                final_riddle_answer = input("Guess again. You only have two remaining guess: ")
                if final_riddle_answer == "a":
                    print("""King Gorgish says; "You are correct! You may return to safety!" \nGorgish's orb glows bright white, the power of the orb pulls you into it. \nYou and the orb are now one! Beams of bright light radiate out of you.\nThe elegant room slowly fades to dark. Suddenly you are transported to the entrance of the maze.\nYou are champion of the Fun Fair Maze!""")
                else:
                    print("""Gorgish says; "Wrong Again!" The elegant shrinks even more. The room now appears to be 5x5 in size.\nYou are worried that if you answer wrong one more time, you'll be smashed into oblivion.""")
                final_riddle_answer = input("Guess again. You have one more guess: ")
                if final_riddle_answer == "a":
                    print("""King Gorgish says; "You are correct! You may return to safety!" \nGorgish's orb glows bright white, the power of the orb pulls you into it. \nYou and the orb are now one! Beams of bright light radiate out of you.\nThe elegant room slowly fades to dark. Suddenly you are transported to the entrance of the maze.\nYou are champion of the Fun Fair Maze!""")
                else:
                    print("""King Gorgish exlaims; Peasant! You have answered incorrectly for a third time!"\nGorgish quickly uses his orb to transport himself out of the room and to safety.\nHe leaves you behind. The room shrinks to the size of an ant.\nYou have been smashed into oblivion.""")



                
            else:
                print("Try Again")
        else:
            print("Try Again")    
    else:
        print("Try again")


        
       
            

room4()