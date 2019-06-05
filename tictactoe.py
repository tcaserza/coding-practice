#
# PROBLEM: Create a tic-tac-toe game with artificial intelligence
#


import random
import copy

class TTTBoard():
    board = None
    open_spaces = []
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        for i in range(3):
            for j in range(3):
                self.open_spaces.append((j,i))

    def add_token(self,location,x_or_o):
        #print "adding token %s in location %s" % (x_or_o,location)
        self.board[location[0]][location[1]] = x_or_o
        self.open_spaces.remove(location)

    def remove_token(self,location):
        #print "removing token %s in location %s" % location
        self.board[location[0]][location[1]] = "-"
        self.open_spaces.append(location)

    def print_board(self):
        for i in range(3):
            print "%s | %s | %s" % (self.board[i][0],self.board[i][1],self.board[i][2])
        print " "

    def check_board_full(self):
        if len(self.open_spaces) == 0:
            return True
        else:
            return False

    def check_winner(self,player):
        for i in range(3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True
        return False


def ai_make_a_move(board):
    if board.check_board_full():
        print "tie game"
        exit(0)
    temp_open_spaces = list(board.open_spaces)
    for space in temp_open_spaces:
        #print "checking space %s,%s" % (space[0],space[1])
        board.add_token(space,"O")
        if board.check_winner("O"):
            #print "found winning move at %s,%s" % (space[0],space[1])
            board.remove_token(space)
            board.add_token(space,"O")
            return
        board.remove_token(space)
        board.add_token(space, "X")
        if board.check_winner("X"):
            #print "found blocking space at %s,%s" % (space[0],space[1])
            board.remove_token(space)
            board.add_token(space, "O")
            return
        board.remove_token(space)
    if (1,1) in board.open_spaces:
        #print "took middle space"
        board.add_token((1,1),"O")
    else:
        random_space = board.open_spaces[random.randint(0, len(board.open_spaces) - 1)]
        #print "took random space %s,%s" % (random_space[0],random_space[1])
        board.add_token(random_space,"O")


if __name__ == "__main__":
    myboard = TTTBoard()
    while not myboard.check_board_full():
        human_move = tuple(int(x.strip()) for x in raw_input("choose location x,y: ").split(','))
        if human_move[0] < 0 or human_move[0] > 2 or human_move[1] < 0 or human_move[1] > 2:
            print "invalid move, try again"
            continue
        if human_move not in myboard.open_spaces:
            print "invalid move, try again"
            continue
        myboard.add_token(human_move,"X")
        myboard.print_board()
        if myboard.check_winner("X"):
            print "human wins"
            break
        ai_make_a_move(myboard)
        myboard.print_board()
        if myboard.check_winner("O"):
            print "ai wins"
            break
