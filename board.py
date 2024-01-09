from player import Player
from crate import Crate

class Board():
    
    def __init__(self):
        
        # made to store the level in a list (is 2D later on)
        self.tiles = []
        # made to store coordinates of crates
        self.crates = []
        self.load_level('level001.xsb')
        print(self.tiles)    
    
        player = Player()
    
#         factor = 64 # factor to increase the pixel position
#         box_pxl_size = 40 # determine size of box
        size = width, height = 1200, 700 # setting screen size
        
        import sys, pygame
        pygame.init()
        
        # loading all the images
#         # scaling them down
        screen = pygame.display.set_mode(size)
        character = pygame.image.load("graphics/character.png")
#         character = pygame.transform.scale(player, (box_pxl_size,box_pxl_size))
        crate = pygame.image.load("graphics/crate.png")
#         crate = pygame.transform.scale(crate, (box_pxl_size,box_pxl_size))
        wall = pygame.image.load("graphics/block.png")
#         wall = pygame.transform.scale(wall, (box_pxl_size,box_pxl_size))
        goal = pygame.image.load("graphics/environment.png")
#         goal = pygame.transform.scale(goal, (box_pxl_size,box_pxl_size))
        ground = pygame.image.load("graphics/ground.png")
#         ground = pygame.transform.scale(ground, (box_pxl_size,box_pxl_size))

        while True:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.tryMovePlayer(0,-1) # YET TO BE MADE
                    elif event.key == pygame.K_DOWN:
                        player.tryMovePlayer(0,1)
                    elif event.key == pygame.K_LEFT:
                        player.tryMovePlayer(1,0)
                    elif event.key == pygame.K_RIGHT:
                        player.tryMovePlayer(-1,0)
                        
            for y in range(0, len(self.tiles)):
                for x in range(0, len(self.tiles[y])):
                    if self.tiles[y][x] == "#":
                        screen.blit(wall, ((16+(64*(x))), (16+(64*(y)))))
                        
            for y in range(0, len(self.tiles)):
                for x in range(0, len(self.tiles[y])):
                    if not self.tiles[y][x] == "#" and ".":
                        screen.blit(ground, ((16+(64*(x))), (16+(64*(y)))))
                        
            for y in range(0, len(self.tiles)):
                for x in range(0, len(self.tiles[y])):
                    if self.tiles[y][x] == "." or self.tiles[y][x] =="*" or self.tiles[y][x] =="+":
                        screen.blit(goal, ((16+(64*(x))), (16+(64*(y)))))
                        
            for y in range(0, len(self.tiles)):
                for x in range(0, len(self.tiles[y])):
                    if self.tiles[y][x] == "$":
                        screen.blit(crate, ((16+(64*(x))), (16+(64*(y)))))
                    elif self.tiles[y][x] == "*":
                        screen.blit(crate, ((16+(64*(x))), (16+(64*(y)))))
                        
            for y in range(0, len(self.tiles)):
                for x in range(0, len(self.tiles[y])):
                    if self.tiles[y][x] == "@":
                        screen.blit(character, ((16 + (64 * (x))), (16 + (64 * (y)))))
                    elif self.tiles[y][x] == "+":
                        screen.blit(character, ((16 + (64 * (x))), (16 + (64 * (y)))))
          

            pygame.display.flip()
            
            
    def load_level(self, levelname):
        
        # load level into 2D-matrix 
        with open(f'levels/{levelname}') as f:
            for line in f:
                # appends list made out of one line
                self.tiles.append([tile for tile in line[:-1]])
                
        for y in self.tiles:
            for x in y:
                if x == "$":
                    c = Crate(x, y)
                    self.crates.append(c)
                
        
        