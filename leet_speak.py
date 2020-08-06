# def exit_key():
#     print(''' "To exit this room you must cypher the code! 
#     ''')
#     leet_speak("fuzzycow")

# leet_dict = {
#     'N' : '4',
#     'W' : '3',
#     'Z' : '6',
#     'F' : '1',
#     'T' : '0',
#     'Y' : '5',
#     'B' : '7',
#     'E' : '9',
#     'A' : '2',
#     'R' : '8'
# }

leet_dict = {
    '4' : 'N',
    '3' : 'W',
    '6' : 'Z',
    '1' : 'F',
    '0' : 'T',
    '5' : 'Y',
    '7' : 'B',
    '9' : 'E',
    '2' : 'A',
    '8' : 'R'
}


def leet_speak(my_string):
    leet_string = ""
    for i in my_string:
        if i.upper() in leet_dict:
            leet_string += (leet_dict[i.upper()])
        else:
            leet_string += (i)
    print(leet_string.capitalize())


my_string = "1u665 co3s 289 i4 0h9 7284"
leet_speak(my_string)

