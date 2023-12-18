import pyfiglet
from colorama import Fore
import time
import random
# __________________________________
# 🟩 TiC Tac Toe چاپ گرافیکی ______
# __________________________________
title=pyfiglet.figlet_format("Tic Tac Toe",font="digital")
print(Fore.GREEN + title)
# __________________________________
# 🟩 آرایه 3 بعدی تخته بازی ______
# __________________________________
game_board=[["⬜️ ","⬜️ ","⬜️ "],
            ["⬜️ ","⬜️ ","⬜️ "],
            ["⬜️ ","⬜️ ","⬜️ "]]
# __________________________________
# 🟩 نمایش تخته بازی _____________
# __________________________________
start_time = time.time()
def show_game_board(WR,pri):
    for i in range(3):
        for j in range(3):
            if WR=="redBeshe":
                if game_board[i][j] == '⬜️ ':
                    game_board[i][j]="🟥 "
            elif WR=="sefidBeshe":
                if game_board[i][j] == '🟥 ':
                    game_board[i][j]="⬜️ "
            else:
                print(game_board[i][j], end=' ')
            if pri=="y":
                print(game_board[i][j], end=' ')
        if pri=="y":
            print()
show_game_board("sefidBeshe","y")
# __________________________________
# 🟩 متن برنده شدن _______________
# __________________________________
def text_barande(barande):
    if barande=="blue":
        print(Fore.RESET+'player wins: 🟦')
    if barande=="green":
        print(Fore.RESET+'player wins: 🟩')
    if barande=="mosavi":
        print(Fore.RESET+'mosavi')
    exit()
# __________________________________
# 🟩 شرط برنده شدن _______________
# __________________________________    
def check_game():
    if game_board[0][0]=="🟦 " and game_board[0][1]=="🟦 " and game_board[0][2]=="🟦 ":
        text_barande("blue")
    elif game_board[1][0]=="🟦 " and game_board[1][1]=="🟦 " and game_board[1][2]=="🟦 ":
        text_barande("blue")
    elif game_board[2][0]=="🟦 " and game_board[2][1]=="🟦 " and game_board[2][2]=="🟦 ":
        text_barande("blue")
    elif game_board[0][0]=="🟦 " and game_board[1][0]=="🟦 " and game_board[2][0]=="🟦 ":
        text_barande("blue")
    elif game_board[0][1]=="🟦 " and game_board[1][1]=="🟦 " and game_board[2][1]=="🟦 ":
        text_barande("blue")
    elif game_board[0][2]=="🟦 " and game_board[1][2]=="🟦 " and game_board[2][2]=="🟦 ":
        text_barande("blue")
    elif game_board[0][2]=="🟦 " and game_board[1][1]=="🟦 " and game_board[2][0]=="🟦 ":
        text_barande("blue")  
    elif game_board[0][0]=="🟦 " and game_board[1][1]=="🟦 " and game_board[2][2]=="🟦 ":
        text_barande("blue") 
    elif game_board[0][0]=="🟩 " and game_board[0][1]=="🟩 " and game_board[0][2]=="🟩 ":
        text_barande("green")
    elif game_board[1][0]=="🟩 " and game_board[1][1]=="🟩 " and game_board[1][2]=="🟩 ":
        text_barande("green")
    elif game_board[2][0]=="🟩 " and game_board[2][1]=="🟩 " and game_board[2][2]=="🟩 ":
        text_barande("green")
    elif game_board[0][0]=="🟩 " and game_board[1][0]=="🟩 " and game_board[2][0]=="🟩 ":
        text_barande("green")
    elif game_board[0][1]=="🟩 " and game_board[1][1]=="🟩 " and game_board[2][1]=="🟩 ":
        text_barande("green")
    elif game_board[0][2]=="🟩 " and game_board[1][2]=="🟩 " and game_board[2][2]=="🟩 ":
        text_barande("green")
    elif game_board[0][2]=="🟩 " and game_board[1][1]=="🟩 " and game_board[2][0]=="🟩 ":
        text_barande("green")  
    elif game_board[0][0]=="🟩 " and game_board[1][1]=="🟩 " and game_board[2][2]=="🟩 ":
        text_barande("green")   
    elif game_board[0][0] != '⬜️ ' and game_board[0][1] != '⬜️ ' and game_board[0][2] != '⬜️ ' and game_board[1][0] != '⬜️ ' and game_board[1][1] != '⬜️ ' and game_board[1][2] != '⬜️ ' and game_board[2][0] != '⬜️ ' and game_board[2][1] != '⬜️ ' and game_board[2][2] != '⬜️ ':
        text_barande("mosavi")
# __________________________________
# 🟩 تعداد بازیکن ________________
# __________________________________
print(Fore.RESET+"game 1 or 2? ")
game=int(input())

def nafarAval():
    while True:
        check_game() 
        row=int(input(Fore.RESET+"row: "))
        col=int(input(Fore.RESET+"col: "))
        if 0<=row<=2 and 0<=col<=2:
            if game_board[row][col]=="⬜️ ":
                game_board[row][col]="🟦 "
                show_game_board("sefidBeshe","y")
                break
            else:
                show_game_board("redBeshe","y")
                print("cell is not empty")
        else:
            show_game_board("redBeshe","y")
            print("just 0,1,2. try again")  
        show_game_board("sefidBeshe","n")         
# __________________________________
# 🟩 نوبت بازی ____________________
# __________________________________
if game==1:
    while True:
        print(Fore.RESET+"player 1:🟦")
        nafarAval()      
        print(Fore.RESET+"player 2:🟩")   
        print(Fore.BLACK+"--- %s seconds ---" % (round(time.time() - start_time))) 
        while True:
            check_game() 
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if 0<=row<=2 and 0<=col<=2:
                if game_board[row][col]=="⬜️ ":
                    game_board[row][col]="🟩 "
                    show_game_board("sefidBeshe","y")
                    break 

elif game==2:
    while True:
        print(Fore.RESET+"player 1:🟦")
        nafarAval()         
        print(Fore.RESET+"player 2:🟩")   
        print(Fore.BLACK+"--- %s seconds ---" % (round(time.time() - start_time))) 
        while True:
            check_game() 
            row=int(input(Fore.RESET+"row: "))
            col=int(input(Fore.RESET+"col: "))
            if 0<=row<=2 and 0<=col<=2:
                if game_board[row][col]=="⬜️ ":
                    game_board[row][col]="🟩 "
                    show_game_board("sefidBeshe","y")
                    break
                else:
                    show_game_board("redBeshe","y")
                    print("cell is not empty")
            else:
                show_game_board("redBeshe","y")
                print("just 0,1,2. try again")  
            show_game_board("sefidBeshe","n")    
        print(Fore.BLACK+"--- %s seconds ---" % (round(time.time() - start_time)))     
