import random

def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)

def isOnlyDigits(num):
    if num == ' ':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')

NUMDIGITS = 3
MAXGUESS = 10

print("I am thinking of a {}-digit number. Try to guess what it is".format(NUMDIGITS))
print("Here are some clues:")
print("When I say:\tThat means:")
print(" Pico\t One digit is correct but in the wrong position.")
print(" Fermi\t One digit is correct and in the right position")
print(" Bagels\t No digit is correct.")

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print("I have thought up a number. you have {} guesses to get it".format(MAXGUESS))

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print("Guess #{}: ".format(numGuesses))
            guess = str(input())

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print("you ran out of guesses. The answer was {}".format(secretNum))

    if not playAgain():
        break
