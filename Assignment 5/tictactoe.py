from tabnanny import check
from colorama import Fore
import time
import random
player = 'player 1 =O'
start_time = time.time()
game = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
# Show game houses and set colors
def show_game_board():
    for i in range(3):
        for j in range(3):
            if game[i][j] == '_':
                print(Fore.BLACK, game[i][j], end=' ')
            elif game[i][j] == 'O':
                print(Fore.BLUE, game[i][j], end=' ')
            else:
                print(Fore.RED, game[i][j], end=' ')
        print()
# Win message and exit the game
def winning_message_player_1():
    textwins = 'player 1 wins'
    print(Fore.BLUE, textwins)
    exit()
def winning_message_player_2():
    textwins = 'player 2 wins'
    print(Fore.RED, textwins)
    exit()
# Check the winner or draw of the game
def check_winner():
    for i in range(3):
        if game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            winning_message_player_2()
        if game[0][i] == 'O' and game[1][i] == 'O' and game[2][i] == 'O':
            winning_message_player_1()
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X':
            winning_message_player_2()
        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O':
            winning_message_player_1()
    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        winning_message_player_2()
    if game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        winning_message_player_1()
    if game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
        winning_message_player_2()
    if game[0][2] == 'O' and game[1][1] == 'O' and game[2][0] == 'O':
        winning_message_player_1()
    if game[0][2] == 'X' and game[1][1] == 'X' and game[2][0] == 'X':
        winning_message_player_2()
    if game[0][0] != '_' and game[0][1] != '_' and game[0][2] != '_' and game[1][0] != '_' and game[1][1] != '_' and game[1][2] != '_' and game[2][0] != '_' and game[2][1] != '_' and game[2][2] != '_':
        print(Fore.GREEN,'draw')
        exit()
# General operation of the game:Check the players' turn-Show board and status-Check the winning or draw status of the game-Check the time elapsed since the start of the game
def game_operation():
    check_turn_of_the_game()
    show_game_board()
    check_winner()
    print(Fore.GREEN, "--- %s seconds ---" % (round(time.time() - start_time)))
# Show game houses and set colors
show_game_board()
# Request a solo game with a computer or doubles
check_single_or_two_player = int(input('Do you play single or double?'))
# Check the turn of the game
def check_turn_of_the_game():
    while True:
        print(Fore.BLACK, player)
        if check_single_or_two_player == 2:
            row = int(input('row: '))
            col = int(input('col: '))
        elif check_single_or_two_player == 1:
            if player == 'player 1 =O':
                row = int(input('row: '))
                col = int(input('col: '))
            elif player == 'player 2 =X':
                row = random.randint(0, 2)
                col = random.randint(0, 2)
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '_':
                if player == 'player 1 =O':
                    z = 'O'
                elif player == 'player 2 =X':
                    z = 'X'
                game[row][col] = z
                break
            else:
                print(Fore.RED, 'You can not. full')
        else:
            print(Fore.RED, 'Just enter between zero and two')
if check_single_or_two_player == 2:
    while True:
        player = 'player 1 =O'
        game_operation()
        player = 'player 2 =X'
        game_operation()
elif check_single_or_two_player == 1:
    while True:
        player = 'player 1 =O'
        game_operation()
        player = 'player 2 =X'
        game_operation()