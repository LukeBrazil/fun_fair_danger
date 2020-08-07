from helper import enter
from termcolor import 

def exit_key():
    enter('''    Oh dear. The wizard has forgotten English.\n
    She has begun to speak Wizard! You still need the secret code to exit her room.''')
    enter('''    But don't be  alarmed. Wizard speak is easy to learn.\n
    Go take a look at the golden tablet hanging on the door.''')  
    print('''

"Psviq 1twyq hspsv wmx eqix, gsrwigxixyv ehmtmwgmrk ipmx. Tippirxiwuyi ujj ijjmgmxyv evgy. Wywtirhmwwi 6ymw yvre jvmrkmppe, ikiwxew svgm rig, psfsvxmw rmfl. Qeyvmw 6x qsppmw ivex. Gvew 5ip yvre zipmx. Ixmeq ceygmfyw pmfivs zip xyvtmw gyvwyw, ex yppeqgsvtiv rmwp gsrwigxixyv. Ryppeq omx eqix pygxyw wetmir. Req 3srzeppmw ivsw e typzmrev gsrwiuyex. Mr silmgype, pmkype tsvxxmxsv tlevixve jivqirxyq, jipmw hspsv jegmpmwmw eykyi, mh kvezmhe ryppe zipmx eg svgm. Wywtirhmwwi 2kix eygxsv zipmx.

"Ryppeq 8y shms iy hmeq kvezmhe xiqtyw ijjmgmxyv iy pmfivs. Hsrig 9ygxyw pis nywxs, zmxei qexxmw hmeq tswyivi jegmpmwmw. Eirier ipmuyix gsrkyi qsppmw. Gyvefmxyv 4vmrkmppe wih tyvyw ix zirirexmw. Hsrig 0sviq ivsw, svrevi rsr megypmw ikix, jmrmfyw uymw uyeq. Hsrig hymw wekmxxmw ib. Ryrg 9ih uyeq zmxei jipmw ipimjirh svrevi fmfirhyq wih mtwyq. Req 7ym erxi, ypxvmgiw ikix xippyw zip, zevmyw ypxvmgmiw ryrg. Qeigirew 2pegivex, qeyvmw e zyptyxexi xmrgmhyrx, zipmx pigxyw zirirexmw hspsv, zip pygxyw evgy rmfl zip wiq. Ziwxmfypyq 8g vmwyw gsqqshs, psfsvxmw evgy ikix, eggyqwer pmkype. Epmuyeq 4y vyxvyq hmeq."\n''')
    print('''    The exit code is embedded in this Wizard speak. Read my instructions carefully.
    --Take the FIRST CHARACTER of the SECOND WORD in EACH SENTENCE
    to make a 21 character code. 
    ''')
    code = input("    Enter code here: ")
    clean_code = no_spaces(code)
    if clean_code == "1u665co3s289i40h97284":
        print()
        print('''    Your passphrase is: {}
        \n'''.format(leet_speak(code)), 'red')
    else:
        print("Try again!")
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
            if i == " ":
                continue
            else:
                leet_string += (i)
    return leet_string.capitalize()

def no_spaces(my_string):
    empty_string = ""
    for i in my_string:
        if i == " ":
            pass
        else:
            empty_string += i
    return empty_string


exit_key()

