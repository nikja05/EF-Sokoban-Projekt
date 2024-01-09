from board import Board

class Movable():
    
    def __init__(self, init_x, init_y):
        board = Board()
        self.x = init_x
        self.y = init_y
    
    def can_move(self, dx, dy):
        
        return False
    
    def move(self, dx, dy):
        
        return False