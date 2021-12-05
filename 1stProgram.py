# Lottery
# Create a program that ask 3 numbers (0-9) from the user
# Generate 3 random winning numbers (0-9)
# Display "Winner" if all 3 input numbers matched the generated numbers
# Display "You loss" if not
# Display "Try again y/n" after each game
# If the user enter "y" the user will play again
# If "n" the program will exit

print('Test your Luck in our Lottery')

import random

def generateThreeNumbers():
    numbers = []
    count = 0
    while count < 3:
        numbers.append(random.randint(0, 10))
        count = count + 1
    return numbers

def getUserInput():
    numbers = []
    count = 0
    while count < 3:
        numbers.append(int(input('Enter your number from 0-9: ')))
        count = count + 1
    return numbers

def displayOutput(winNumbersF, userNumbersF):
    playAgain = 'y'
    while playAgain[0] == 'y':
        if winNumbersF == userNumbersF:
            print('Winner!')
        else:
            print('You lose!')
        playAgain = input('Try again? (y or no): ')


winningN = generateThreeNumbers()
userN = getUserInput()
displayOutput(winningN, userN)

print('Thank you for participating in our lottery!')