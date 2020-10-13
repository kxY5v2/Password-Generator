'''This program will generate a password based on the parameters:
    number of characters
    include numbers
    include letters
    include specialty characters
'''

import random

# Key Sets
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=']

# Parameters
validAnswers = {'y': 1, 'n': 1}

def getParameters():
    global incNums
    global incLetters
    global incSymbols
    global numCharacters
    try:
        incNums = input('Include Numbers in Password (y/n): ')
        validAnswers[incNums]
    except KeyError:
        print('You did not enter a valid choice')

    try:
        incLetters = input('Include Letters (y/n): ')
        validAnswers[incLetters]
    except KeyError:
        print('You did not enter a valid choice')

    try:
        incSymbols = input('Include Symbols (y/n): ')
        validAnswers[incSymbols]
    except KeyError:
        print('You did not enter a valid choice')

    try:
        numCharacters = int(input('How many chacters would like you the password to be: '))
    except ValueError:
        print('Answer is not an integer.')


# Find which array will need:
def findSet(incNums, incLetter, incSymbols):
    # All true
    if incNums == 'y' and incLetter == 'y' and incSymbols == 'y':
        set = numbers + letters + symbols
    # Numbers True
    elif incNums == 'y' and incLetter == 'y' and incSymbols == 'n':
        set = numbers + letters
    elif incNums == 'y' and incLetter == 'n' and incSymbols == 'y':
        set = numbers + symbols
    elif incNums == 'y' and incLetter == 'n' and incSymbols == 'n':
        set = numbers
    # Letters True
    elif incNums == 'n' and incLetter == 'y' and incSymbols == 'y':
        set = letters + symbols
    elif incNums == 'n' and incLetter == 'y' and incSymbols == 'n':
        set = letters
    # Symbols True
    elif incNums == 'n' and incLetter == 'n' and incSymbols == 'y':
        set = symbols
    else:
        getParameters()
    return set


def generatePass(set):
    password = ''.join([random.SystemRandom().choice(set) for _ in range(numCharacters)])
    return password


def addToFile(password):
    with open('PasswordList.txt', 'a+') as file:
        file.write(password + '\n')


def main():
    getParameters()
    set = findSet(incNums, incLetters, incSymbols)
    password = generatePass(set)
    print('Password Generated: ' + password + '\n')
    print('All passwords generated will be written to file PasswordList.txt for future reference.')
    addToFile(password)


main()
