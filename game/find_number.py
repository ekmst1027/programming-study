import random

guessesTaken = 0

print("Hello! What is your name?")
player_name = input()

number = random.randint(1, 20)

print("Well, {}, I am Thinking of a number between 1 and 20")

while guessesTaken < 6:
    print("Take a guess.")
    guess = int(input())

    guessesTaken += 1

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessesTaken)
    print('Good job, {}! You guessed my number in {} guesses!'.format(player_name, guessesTaken))

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was {}'.format(number))
