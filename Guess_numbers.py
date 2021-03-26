## Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

import random
import math
# taking inputs
lower = int(input('Enter minimum number: '))
upper = int(input('Enter maximum number: '))
# generating random numbers
x = random.randint(lower, upper)
print('\n\t You have only ', round(math.log(upper - lower + 1, 2)), 'chances to guess the number.')
count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input('Enter a number:'))

    if x == guess:
        print('Congratulaitons! You have guessed the number')
        break
    
    elif x > guess:
        print("This is too low to guess")
    elif x < guess:
        print('This is too big to guess')

    if count >= math.log(upper-lower+1, 2):
        print('\n\t The number for you are tring is %d', x)
        print("\n\t Better luck next time. Good bye")

    