import sys, pygame
pygame.init()

x, y = 0, 0 # initializing the coordinates for the loop
factor = 40 # factor to increase the pixel position
box_pxl_size = 40 # determine size of box
size = width, height = 800, 500 # setting screen size

# loading all the images
screen = pygame.display.set_mode(size)
player = pygame.image.load("graphics/player.png")
player = pygame.transform.scale(player, (box_pxl_size,box_pxl_size))
crate = pygame.image.load("graphics/crate.png")
crate = pygame.transform.scale(crate, (box_pxl_size,box_pxl_size))
wall = pygame.image.load("graphics/block.png")
wall = pygame.transform.scale(wall, (box_pxl_size,box_pxl_size))
goal = pygame.image.load("graphics/environment.png")
goal = pygame.transform.scale(goal, (box_pxl_size,box_pxl_size))
ground = pygame.image.load("graphics/ground.png")
ground = pygame.transform.scale(ground, (box_pxl_size,box_pxl_size))


with open('levels/level001.xsb') as f:
    for line in f:
        for sign in line:
            
            if sign == "@":
                screen.blit(player, (x*factor,y*factor))
                
            if sign == "$":
                screen.blit(crate, (x*factor,y*factor))
                
            if sign == "#":
                screen.blit(wall, (x*factor,y*factor))
                
            if sign == " " or "":
                screen.blit(ground, (x*factor,y*factor))
                
            if sign == ".":
                screen.blit(goal, (x*factor,y*factor))
                    
            x += 1
            
        y += 1
        x = 0
        
    pygame.display.flip()

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.tryMovePlayer(0,-1)
                elif event.key == pygame.K_DOWN:
                    player.tryMovePlayer(0,1)
                elif event.key == pygame.K_LEFT:
                    player.tryMovePlayer(1,0)
                elif event.key == pygame.K_RIGHT:
                    player.tryMovePlayer(-1,0)
