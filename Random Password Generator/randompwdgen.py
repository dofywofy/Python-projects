
'''
Random Password Generator using Python
Made by Strygwyr
'''

import random, string

print('Hello, Welcome to Random Password Generator')

length = int(input('\nEnter the length of the password: '))

strength = int(input('\nPlease enter the strength of the password: \n1. Weak\n2. Strong \n3.Very strong \n'))

pwd = list()

def password(length, num=False, strength=True):
    """Length of the password, num if you want a number,
        strength (weak, strong, very strong)"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == '1':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)

    elif strength == '2':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)

    elif strength == '3':
        ran = randint(2,4)
        if num:
            length -= ran
            for i in range(ran):
                pwd = random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letter)

    random.shuffle(pwd)
    return ''.join(pwd)        
