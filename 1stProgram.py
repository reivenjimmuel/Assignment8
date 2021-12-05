import random

def gameFunc():

    # Get user 3 guesses of numbers from 0-9
    userN = []
    userGuesses = 0
    while userGuesses < 3:
        userN.append(int(input('Enter your number from 0-9: ')))
        userGuesses = userGuesses + 1

    # Generate 3 random numbers from 0-9
    generatedN = []
    count = 0
    while count < 3:
        generatedN.append(random.randint(0, 10))
        count = count + 1

    # Check if the user's guess is within the generated numbers
    # Return the total number of correct guesses
    correctGuessN = 0
    for n in userN:
        if n in generatedN:
            correctGuessN = correctGuessN + 1
        else:
            correctGuessN = correctGuessN 
    return correctGuessN

def displayOutput():

    # Evaluate if the user won the lottery or not
    # Interactive loop to ask if the user want to try again or not
    playAgain = 'Y'
    while playAgain[0] == 'Y':
        userScore = gameFunc()
        if userScore == 3:
            print('Winner!')
        else:
            print('You lose!')
        playAgain = input('Try again? (y or n): ').upper()

print('Test your luck in the Lottery Game!')
displayOutput()
print('Thank you for participating in our lottery!')