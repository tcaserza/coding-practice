#
# Problem: Create a minesweeper game
#
import random


class MinesweeperBoard:
    visible_board = None
    master_board = None
    total_mines = None
    mines_left = None
    x = 0
    y = 0
    available_spots_left = 0
    
    def __init__(self, x, y, mines):
        self.x = x
        self.y = y
        self.total_mines = mines
        self.mine_locations = []
        self.generate_board(x, y, mines)
        self.generate_blank_board(x, y)
        self.available_spots_left = (x * y) - mines

    def generate_board(self,x, y, mines):
        self.master_board = [["0" for _i in range(y)] for _j in range(x)]
        for i in range(0, mines):
            mine_x = random.randint(0, x-1)
            mine_y = random.randint(0, y-1)
            while (mine_x, mine_y) in self.mine_locations:
                mine_x = random.randint(0, x - 1)
                mine_y = random.randint(0, y - 1)
            self.master_board[mine_x][mine_y] = "X"
            self.mine_locations.append((mine_x, mine_y))
            if mine_x >= 1 and (mine_x - 1,mine_y) not in self.mine_locations:
                self.master_board[mine_x - 1][mine_y] = str(int(self.master_board[mine_x - 1][mine_y]) + 1)
            if mine_x + 1 < self.x and (mine_x + 1,mine_y) not in self.mine_locations:
                self.master_board[mine_x + 1][mine_y] = str(int(self.master_board[mine_x + 1][mine_y]) + 1)
            if mine_y >= 1 and (mine_x,mine_y - 1) not in self.mine_locations:
                self.master_board[mine_x][mine_y-1] = str(int(self.master_board[mine_x][mine_y-1]) + 1)
            if mine_y+ 1 < self.y and (mine_x,mine_y + 1) not in self.mine_locations:
                self.master_board[mine_x][mine_y+1] = str(int(self.master_board[mine_x][mine_y+1]) + 1)
    
    def generate_blank_board(self, x, y):
        self.visible_board = [["-" for _i in range(x)] for _j in range(y)]
    
    def print_board(self):
        for i in range(0, self.x):
            line = []
            for j in range(0, self.y):
                line.append(self.visible_board[j][i])
            print line


if __name__ == "__main__":
    board_dimensions = (8,8)
    num_mines = 5
    board = MinesweeperBoard(board_dimensions[0], board_dimensions[1],num_mines)
    board.print_board()
    while board.available_spots_left > 0:
        print board.mine_locations
        selection = tuple(int(input.strip()) for input in raw_input("x,y:").split(','))
        visual_selection = (selection[1],selection[0])
        if selection in board.mine_locations:
            print "Boom, game over"
            exit(0)
        else:
            board.visible_board[visual_selection[1]][visual_selection[0]] = board.master_board[visual_selection[1]][visual_selection[0]]
            board.print_board()
    print "You win, game over"