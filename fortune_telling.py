from helper import enter
import random

def fortune_topic():
    topics = ["love", "money", "happiness"]
    love_wealth_happiness = ""
    while love_wealth_happiness not in topics:
        love_wealth_happiness = enter('"There is a lot to tell you but we don\'t have much time. Would you like to learn about love, money, or happiness?"\n').lower()
        if love_wealth_happiness in topics:
            enter(f"{love_wealth_happiness.title()} it is.")
            enter(random_quote(love_wealth_happiness))
        else:
            enter("Please spell correctly!")
    
## Random quote generator 
def random_quote(flag):
    my_dict = {
    "money" : ["1", "2", "3", "4", "5"],
    "love" : ["1", "2", "3", "4", "5"],
    "happiness" : ["1", "2", "3", "4", "5"]
    }
    return random.choice(my_dict[flag])
    

fortune_topic()


