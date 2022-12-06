import os
import random
import string
import time
import sys
def hapus():
    os.system('cls')

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
animation = ["[■□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□]", "[■■■□□□□□□□□□□□□]",
"[■■■■□□□□□□□□□□□]","[■■■■■□□□□□□□□□□]", "[■■■■■■□□□□□□□□□]", "[■■■■■■■□□□□□□□□]", 
"[■■■■■■■■□□□□□□□]", "[■■■■■■■■■□□□□□□]", "[■■■■■■■■■■□□□□□]","[■■■■■■■■■■■□□□□]",
"[■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■]"]
def load():
    for i in range(len(animation)):
        time.sleep(0.17)
        sys.stdout.write("\r Generating " + animation[i % len(animation)])
        sys.stdout.flush()


def menu():
    hapus()
    hapus()
    print('''
======================
| Password Generator |
|====================|
|    <1> Generate    |
|    <2> Quit        |
======================\n''')
    pilih = input('----> ')
    if pilih == '1':
        generate()
    elif pilih == '2':
        quit('Thanks for using this, See you next time :))')
    else:
        print()
        input('Error, Please Return')
        menu()

def generate():
    print('='*30)
    try:
        length = int(input('\nEnter the length of password: '))
        if length < 1:
            input('Cant create a password below -1 character')
            generate()
        elif length > 94:
            input('Too many characters')
            generate()
        else:
            exe = random.sample(all, length)
            password = ''.join(exe)
            hapus()
            load()
            print(f'''
        ========================
        Password: {password}
        ========================''')
            tryit()
    except:
        input('Must be numbers')
        generate()

def tryit():
    loop = input('Again? > ')
    if loop == 'y' or loop == 'Y' or loop == 'Yes' or loop == 'yes' or loop == 'yEs' or loop == 'YeS' or loop == 'yeS' or loop == 'YES':
        generate()
    elif loop == 'n' or loop == 'N' or loop == 'No' or loop == 'no' or loop == 'nO' or loop == 'NO':
        quit('Thanks for using this, See you next time :))')
    else:
        print()
        input('Error, Try again')
        tryit()

def quit(s):
    hapus()
    print()
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)

menu()