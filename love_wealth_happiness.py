def fortune_topic():
    love_wealth_happiness = ""
    while love_wealth_happiness != 'love' and love_wealth_happiness != 'money' and love_wealth_happiness != 'happiness':
        love_wealth_happiness = input('"There is a lot to tell you but we don\'t have much time. Would you like to learn about love, money, or happiness?"\n').lower()
        if love_wealth_happiness == 'love':
            answer = 'Love'
            print(f"{answer} it is. Please tell me a number (1-5)")
            break
        elif love_wealth_happiness == 'money':
            answer = 'Money'
            print(f"{answer} it is. Please tell me a number (1-5)")
            break
        elif love_wealth_happiness == 'happiness':
            answer = 'Happiness'
            print(f"{answer} it is. Please tell me a number (1-5)")
            break
        else:
            print("Please spell correctly!")
    
fortune_topic()