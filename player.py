import math
import random

class player:
    #intialize player letter X or O
    def __init__(self, letter):
        self.letter= letter
        
    #players next move
    def get_next_move(self, game):
        pass

class computerplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_next_move(self, game):
        
        square = random.choice(game.free_moves())
        return square
    
class secondplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_next_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
             #check if the value is correct by inserting an interger and return invalid if not
             #check for available spot on the board and return invalid 
            try:
                val = int(square)
                if val not in game.free_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Move. Try again')
        
        return val
            
    