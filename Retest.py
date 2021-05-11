# Testing out Pycharm with a guessing game

from random import randint
guessed = False
number = randint(0, 100)
guesses = 0
while not guessed:
    ans = input("Try to guess the number I am thinking of!")
    # use tab to indent
    guesses += 1
    if int(ans) == number:
        print("Congrats! You Got it!")
        # Use tab twice to indent twice
        print("It took you {} guesses!".format(guesses))
        break
    elif int(ans) > number:
        print("The number is lower than what you guessed.")
    elif int(ans) < number:
        print("The number is greater than what you guessed.")
