from time import sleep
import os


def sleep_and_clear(sleep_seconds:float=1.5):
    sleep(sleep_seconds)
    os.system('cls')

def creating_the_board():
    count = 0
    board = []
    for x in range(11):
        if count == 0:
            letters = "    A  B  C  D  E  F  G  H  I  J"
            board.append(letters)
        else:
            row = "[ ]"*10
            if count == 10:
                board.append(f"{count} {row}")
            else:
                board.append(f"{count}  {row}")
        count += 1
    return board

def actual_board_printer(board):
    for x in board:
        print(x)

def changing_the_board(board:list,x:int,y:str):
    x = int(x)
    position_of_letter = board[0].index(y.upper())
    new_row = board[x]
    new_row = new_row[:position_of_letter] + "x" + new_row[position_of_letter+1:]
    board.remove(board[x])
    board.insert(x,new_row)

def placing_the_boats(board,player):
    count = 1
    while True:
        print(f"PLAYER {player}".center(32))
        actual_board_printer(board)
        if count == 1:
            what_boat = "lilla"
        if count == 2:
            what_boat = "mellan"
        if count == 3:
            what_boat = "stora"
        if count == 4:
            print("Dina placeringar, tryck enter för att komma vidare")
            japp = input("")
            break
        print(f"Båtar: [X]      [X][X]      [X][X][X]")
        print(f"Ange vart du vill placera {what_boat} båten")
        for x in range(count):
            x,y = input("").split()
            changing_the_board(board,x,y)
        sleep_and_clear(0)
        count += 1
        

board1 = creating_the_board()
board1_hits = creating_the_board()
board2 = creating_the_board()
voard2_hits = creating_the_board

# for x,y in zip(board1,board2):
#     print(x,y)

while True:
    #Spelare 1
    placing_the_boats(board1,1)
    placing_the_boats(board2,2)

    hejeheej = input("")


    

# print(board1[0].replace(" ", "")[2])

# actual_board_printer(board1)

# while True:
#     actual_board_printer(board1)
