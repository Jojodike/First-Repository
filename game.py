import time
from player import secondplayer, computerplayer

class TicTacToe: 
    def __init__(self):
        self.board = [' ' for _ in range(9)]  #initialize list rep of 3 x 3 board
        self.current_winner = None # keep track of the current winner
    
    def print_board(self):
        for row in (self.board[i*3:(i+1)*3] for i in range(3)):
            print (' | ' + ' | '.join(row) + ' | ')
            
    @staticmethod
    def print_board_no():
        # corresponding box numbers
        board_number = [[str(i) for i in range (j*3, (j+1)*3)] for  j in range(3)]
        for row in board_number:
            print(' | ' + ' | '.join(row) + ' | ')
    #game logic        
    def free_moves(self):
        # intitialize moves to list[]
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def number_empty(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # assign square to letter for if move is valid or false if not
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter): 
        
        #check for winner with 3 matches in a row on the board
        row_ind = square // 3
        row= self.board[row_ind*3 : (row_ind + 1)*3]
        if all ([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square %3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all ([spot == letter for spot in column]):
            return True
        
        #check diagonals of even square numbers (0, 2, 4, 6, 8)
        if square %2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all ([spot == letter for spot in diagonal1]):
                return True
            diagonal2= [self.board[i] for i in [2, 4, 6]]
            if all ([spot == letter for spot in diagonal2]):
                return True
        #if checks fails
        return False
    
def play(game, x_player, o_player, print_game=True):
    #return winner of the game or none for tie
    if print_game:
        game.print_board_no()
        
    letter = 'O' #first letter
    
    #iterates game while with empty squares
    while game.empty_squares():
        
        #get current player move 
        if letter == 'X':
            square = x_player.get_next_move(game)
        else:
            square = o_player.get_next_move(game)
            
        #define functon to make a move on the board
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('') #empty line
                
            if game.current_winner:
                if print_game:
                    print(letter + 'wins!')
                return letter
            
             #player switches  
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
    
        time.sleep(0.8) #pause
              
    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    o_player = secondplayer('X')
    x_player = computerplayer('O')
    t = TicTacToe()
    play(t, o_player, x_player, print_game=True)