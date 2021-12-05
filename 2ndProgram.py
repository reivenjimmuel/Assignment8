import random

def evaluateUserGuess():

    # Generate a random number from 0 to 100
    number = random.randint(0, 101)

    # Evaluate the user's input together with the generated number
    # Print output
    status = 'FALSE'
    while status == 'FALSE':
        userGuess = int(input('What number do I currently have?: '))
        if userGuess > number:
            print('Your guess is greater than my number. Try again!')
        elif userGuess < number:
            print('Your guess is lower than my number. Try again!')
        else:
            print('''
Congratulations! You guessed my number correctly!

Thanks for playing with me! Till next time!
            ''')
            status = 'TRUE'

print('''
Let's play GUESS THE NUMBER!

Try to guess the number that I am thinking from 0 to 100.

Good luck!
''')
evaluateUserGuess()