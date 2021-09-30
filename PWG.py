
'''
Random Password Generator using Python
Made by Strygwyr
'''

import random, string

print('Hello, Welcome to Random Password Generator.')

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
dig = list(string.digits)
punct = list(string.punctuation)
password = []

def generatePassword(passwordLength, useUppercase, useLowercase, useNumbers, usePunctuations, password):
    charsToUse = []
    if useUppercase == True:
        charsToUse.extend(upper)
    if useLowercase == True:
        charsToUse.extend(lower)
    if useNumbers == True:
        charsToUse.extend(dig)
    if useSymbols == True:
        charsToUse.extend(punct)

    while int(passwordLength) > len(password):
        password.append(random.choice(charsToUse))

    random.shuffle(password)
    return password

passwordLength = input('How long would you like the password to be?: ')
useUppercase = bool(input('Do you require Uppercase letters? 1=Yes, Leave Blank=No: '))
useLowercase = bool(input('Do you require Lowercase letters? 1=Yes, Leave Blank=No: '))
useNumbers = bool(input('Do you require Numbers? 1=Yes, Leave Blank=No: '))
useSymbols = bool(input('Do you require Symbols? 1=Yes, Leave Blank=No: '))

Plist = generatePassword(passwordLength, useUppercase, useLowercase, useNumbers, useSymbols, password)
print(''.join(Plist))
