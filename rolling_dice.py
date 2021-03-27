<bold>This is a classic roll the dice program We will be using the random module for this, since we want to randomize the numbers we get from the dice.<bold>

import random

mini = 1
maxi = 6

rolling = 'Yes'

while rolling == "Yes" or rolling == 'y':
    print('Rolling the dice..')
    print('\tHere are the values: ')
    print(random.randint(mini, maxi))
    print(random.randint(mini, maxi))
    break


