def room4():
    print("""After a long and daunting journey through the Fun Fair Maze, you have entered the fourth and final room! \n You notice this is a room of elegance.\nThe white marble tiled floors are accented with gold and the walls are covered with pristine art from around the world.\nIn the middle of the room, hangs a large diamond chandelier. \n After looking around for a few moments, you estimate that this room is about 20x20 feet. \n \n All of a sudden, a large troll dressed in garments and robes of royalty forms from the marble floors directly beneath the chandelier. The troll is holding some sort of glowing angelic orb. \n The troll exclaims; "I am Gorgish, King of the Fun Fair Maze! In order to exit the maze, you must give me the three items you've acquired from the former rooms. Then you must answer my riddle that only a true Fun Fair Maze Champion would know. If you guess correctly, my orb will wisk you away to safety. Beware, you will only get three guesses to answer my riddle correctly, if you fail, you will be crushed into oblivion.""")
    
    room1_unlocked = input(""" Gorgish asks; "What is the passcode from room 1?" """)
    
    # The troll is asking if you for the correct code from room 1
    room1answer = room1_unlocked
    if room1answer in ["Fuzzy cows are in the barn", "fuzzy cows are in the barn", "Fuzzy Cows Are In The Barn"]:
        print("Excellent. Your passcode is correct")
        #The troll is asking if you brought the correct item from room2
        room2_unlocked = input(""" Gorgish asks; "What did you bring me from room 2?" """)
        room2answer = room2_unlocked
        if room2answer in ["Golden axe", "golden axe", "Golden Axe", "GOLDEN AXE", "GoldenAxe"]:
            print("Excellent. You hand it over to Gorgish. Trolls are so greedy.")
            #The troll is asking if you brought the correct item from room3
            room3_unlocked = input(""" Gorgish asks; "What did you bring me from room 3?" """)
            room3answer = room3_unlocked
            if room3answer in ["Golden Tomato", "golden tomato", "GOLDEN TOMATO"]:
                print("Excellent! You have moved onto the final challange: The Fun Fair Maze Riddle.")
                #the troll is asking the final riddle
                final_riddle_answer = input(""" Gorgish says; "Such amazing loot you have brought to me! Here is your Final Riddle:\n "I have numerous teeth\nAnd I'm kept on a chain\nI'm the singer's delight\nAnd the burglar's disdain... \nWhat is your answer?" """)
                answer = final_riddle_answer
                if answer in ["A key", "a key", "A KEY", "A Key"]:
                    print("""***********************\nKing Gorgish says; "You are correct! You may return to safety!" \nGorgish's orb glows bright white, the power of the orb pulls you into it. \nYou and the orb are now one! Beams of bright light radiate out of you.\nThe room of elegance slowly fades to dark. Suddenly you are transported to the entrance of the maze.\nYOU ARE CHAMPION OF THE FUN FAIR MAZE!""")
                else:
                    print("""XXXXXXXXXXXXXXXXXXXXXXXXX\nGorgish says; "Wrong!" The elegant room shrinks drastically. The room now appears to be 10x10 in size.\nYou are worried if you answer wrong two more times, you'll be smashed into oblivion.""")
                
                    final_riddle_answer = input("XXXXXXXXXXXXXXXXXXXXXXXX\nGuess again. You only have two remaining guess: ")
                    answer = final_riddle_answer
                    if answer in ["A key", "a key", "A KEY", "A Key"]:
                        print("""*************************\nKing Gorgish says; "You are correct! You may return to safety!" \nGorgish's orb glows bright white, the power of the orb pulls you into it. \nYou and the orb are now one! Beams of bright light radiate out of you.\nThe elegant room slowly fades to dark. Suddenly you are transported to the entrance of the maze.\nYOU ARE CHAMPION OF THE FUN FAIR MAZE!""")
                    else:
                        print("""XXXXXXXXXXXXXXXXXXXXXXXXXXX\nGorgish says; "Wrong Again!" The elegant shrinks even more. The room now appears to be 5x5 in size.\nYou are worried that if you answer wrong one more time, you'll be smashed into oblivion.""")
                        final_riddle_answer = input("XXXXXXXXXXXXXXXXXXXXXXXX\nGuess again. You have one more guess: ")
                        answer = final_riddle_answer
                        if answer in ["A key", "a key", "A KEY", "A Key"]:
                            print("""*****************************\nKing Gorgish says; "You are correct! You may return to safety!" \nGorgish's orb glows bright white, the power of the orb pulls you into it. \nYou and the orb are now one! Beams of bright light radiate out of you.\nThe elegant room slowly fades to dark. Suddenly you are transported to the entrance of the maze.\nYOU ARE CHAMPION OF THE FUN FAIR MAZE!""")
                        else:
                            print("""XXXXXXXXXXXXXXXXXXXXXXXXXXXX\nKing Gorgish exlaims; Peasant! You have answered incorrectly for a third time!"\nGorgish quickly uses his orb to transport himself out of the room and to safety.\nHe leaves you behind. The room shrinks to the size of an ant.\nYou have been smashed into oblivion.""")
                        


            else:
                print("Try again")
                room4()
                
        else:
            print("Try Again") 
            room4()
               
    else:
        print("Try again")
        room4()
        


room4()