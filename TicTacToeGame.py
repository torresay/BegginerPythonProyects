from time import time
from TicTacToePlayer import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:

    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)] # we eill se a single list to rep 3x3 board
        self.current_winner = None # keep track of the winner
    
    def print_board(self):
        # this is getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0  | 1 | 2, telling us what number correspons to what box
        number_board = [[str(i) for i in range (j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def avaliable_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then returns true. If invalida, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere and we have to check all of these
        # first check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals 
        # but only if squares is an even numebr (0, 2, 4, 6,8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False # because it means that we don't have a winner yet



def play(game, x_player, o_player, print_game = True):
    if print_game:
        TicTacToe.print_board_nums()
    
    letter = 'X' #starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about winner because we'll just return that which breaks the loop)
    while TicTacToe.empty_squares():
        # get the move drom the appropiate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # let's define a function to make a move!
        if TicTacToe.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                TicTacToe.print_board()
                print('')
            
            if TicTacToe.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter
            
            # after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # Switches player
        
        time.sleep(0.8)

    if print_game:
        print('It is a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)