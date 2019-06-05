#
# Problem: Create a minesweeper game
#

import random

def generate_board(x,y, mines):
    board = [["0" for i in range(x)] for j in range(y)]
    for i in range(0,mines):
        mine_x = random.randint(0,x-1)
        mine_y = random.randint(0,y-1)
        print mine_x,mine_y
        board[mine_y][mine_x] = "X"
    for i in range(y):
        for j in range(x):
            adjacent_mines = 0
            if board[i][j] == "X":
                continue
            if i - 1 >= 0 and board[i-1][j] == "X":
                adjacent_mines += 1
            if i + 1 < x and board[i+1][j] == "X":
                adjacent_mines += 1
            if j - 1 >= 0 and board[i][j-1] == "X":
                adjacent_mines += 1
            if j + 1 < y and board[i][j+1] == "X":
                adjacent_mines += 1
            board[i][j] = str(adjacent_mines)
    return board

def print_board(board):
    for i in range (0,len(board)):
        print board[i]



if __name__ == "__main__":
    board_dimensions = (8,8)
    master_board = generate_board(board_dimensions[0],board_dimensions[1],2)
    visible_board = [["A" for i in range(board_dimensions[0])] for j in range(board_dimensions[1])]
    print_board(visible_board)
    mine_hit = False
    spots_left = board_dimensions[0] * board_dimensions[1]
    while not mine_hit:
        selection = tuple(int(x.strip()) for x in raw_input("x,y:").split(','))
        if master_board[selection[1]][selection[0]] == "X":
            print "Boom, game over"
            exit(0)
        else:
            visible_board[selection[1]][selection[0]] = master_board[selection[1]][selection[0]]
            print_board(visible_board)