## Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

player1_call = input("Player1: Enter rock/paper/scissor: ")
player2_call = input("Player2: Ener rock/papper/scissor: ")

def rock_papper_scissor(player1, player2):
    item_list = ['rock', 'scissor', 'papper']

    while player1 not in item_list or player2 not in item_list:
        print("Invalid: Please enter a valid name:")
        player1_call = input("Player1: Enter rock/papper/scissor:")
        player2_call = input('Player2: Enter rock/papper/scissor')

    if player1 == player2:
        print('Invalid Command: Please enter a valid command')
        player1 = input("Player1: Enter rock/papper/scissor")
        player2 = input('Player2: Enter rock/papper/scissor')

    if player1 == 'rock' and player2 == 'papper':
        print('Player No.1 Wins')
    
    elif player1 == 'rock' and player2 == 'scissor':
        print("Player No.1 Wins")
    
    elif player1 == 'papper' and player2 == 'scissor':
        print('Player No. 2')
    
    elif player1 == 'papper' and player2 == 'rock':
        print('Player No.2 wins')
    
    elif player1 == 'scissor' and player2 == 'papper':
        print('Player No.1 Wins')
    
    elif player1 == 'scissor' and player2 == 'rock':
        print('Player No. 2 Wins')



rock_papper_scissor(player1_call, player2_call)