from helper import enter
from pip._vendor.colorama import Fore, Back, Style


def exit_key():
    enter('''    Oh dear. The wizard has forgotten English.\n
    She has begun to speak Wizard! You still need the secret code to exit her room.''')
    enter('''    But don't be  alarmed. Wizard speak is easy to learn.\n
    Go take a look at the marble tablet hanging on the door.''')  
    print(Back.BLACK + Fore.MAGENTA + '''

"Psviq 4twyq hspsv wmx eqix, gsrwigxixyv ehmtmwgmrk ipmx. Tippirxiwuyi 8jj ijjmgmxyv evgy. Wywtirhmwwi lymw yvre jvmrkmppe, ikiwxew svgm rig, psfsvxmw rmfl. Qeyvmw 0x qsppmw ivex. Gvew 9ip yvre zipmx. Ixmeq 6eygmfyw pmfivs zip xyvtmw gyvwyw, ex yppeqgsvtiv rmwp gsrwigxixyv. Ryppeq 3mx eqix pygxyw wetmir. Req 5srzeppmw ivsw e typzmrev gsrwiuyex. Mr zilmgype, pmkype tsvxxmxsv tlevixve jivqirxyq, jipmw hspsv jegmpmwmw eykyi, mh kvezmhe ryppe zipmx eg svgm. Wywtirhmwwi 2kix eygxsv zipmx.

"Ryppeq 7y shms iy hmeq kvezmhe xiqtyw ijjmgmxyv iy pmfivs. Eirier 0pmuyix gsrkyi qsppmw."''')
    print(Fore.WHITE + Back.BLACK)
    print(Fore.WHITE + Back.BLACK + '''\n    The exit code is embedded in this Wizard speak. Read my instructions carefully.\n
    --Take the FIRST CHARACTER of the SECOND WORD in EACH SENTENCE
    to make a 12 character code. \n
    --You only have 3 tries, so yes, be careful!
    ''')
    # code = input("    Enter code here: ")
    # clean_code = no_spaces(code)

    acc = 0
    countdown = 3
    while acc < 3:
        code = input("    Enter code here: ")
        print()
        clean_code = no_spaces(code)
        if clean_code == "48l09635z270":
            print()
            print('''    Your passphrase is: {}
            \n'''.format(leet_speak(code)))
            enter(Fore.WHITE + "The door opens!")
            break
        elif clean_code == "cheatcode":
            print()
            print("    Your passphrase is: " + Fore.YELLOW + "goldenwizard" + Fore.WHITE)
            enter(Fore.WHITE + "The door opens!")
            break
        else:
            acc += 1
            countdown -= 1
            print(f"Try again! You have {countdown} tries left!\n")
            if countdown == 0:
                print("Game over! You are stuck in the wizard room forever.")
                exit()

leet_dict = {

    '4' : 'G',
    '3' : 'W',
    '6' : 'N',
    '1' : 'F',
    '0' : 'D',
    '5' : 'I',
    '7' : 'R',
    '9' : 'E',
    '2' : 'A',
    '8' : 'O'
}


def leet_speak(my_string):
    leet_string = ""
    for i in my_string:
        if i.upper() in leet_dict:
            leet_string += (leet_dict[i.upper()])
        else:
            if i == " ":
                continue
            else:
                leet_string += (i)
    return Fore.YELLOW + leet_string.lower()

def no_spaces(my_string):
    empty_string = ""
    for i in my_string:
        if i == " ":
            pass
        else:
            empty_string += i
    return empty_string


# exit_key()

