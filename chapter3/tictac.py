import random

class Game:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.log = True 
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]

    def show_board(self):
        for row in self.board:
            print(row)

    def cek_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.log = False
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.log = False
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.log = False
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.log = False

    def cek_update(self,player,row,column):
        print(f"Player {player.name} move: {row},{column}")
        if self.board[row][column] == 0:
            self.board[row][column] = 1 if player == self.p1 else 2
        else:
            print("Invalid move! Cell already occupied.")

    def run(self):
        while(self.log):
            self.cek_update(self.p1, *self.p1.move(self.board))
            self.show_board()
            self.cek_winner()
            self.cek_update(self.p2, *self.p2.move(self.board))
            self.show_board()
            self.cek_winner()

class RandomPlayer:
    def __init__(self, name):
        self.name = name

    def move(self, board):
        row = random.randint(0,2)
        col = random.randint(0,2)
        return row, col

random_player1 = RandomPlayer("Player 1")
random_player2 = RandomPlayer("Player 2")
game = Game(random_player1, random_player2)
game.run()