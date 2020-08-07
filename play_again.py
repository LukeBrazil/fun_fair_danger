def play_again():
    x = input("Would you like to play again? ")
    if x in ["Yes", "yes", "Y", "y", "YES"]:
        run_fortune_teller()
    else:
        print("Ok. Come back another time!")


play_again()