import sys, pygame
pygame.init()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
player = pygame.image.load("graphics/player.png")
crate = pygame.image.load("graphics/crate.png")
wall = pygame.image.load("graphics/block.png")
#ground = pygame.image.load("graphics/ground.png")
goal = pygame.image.load("graphics/environment.png")

x, y = 0, 0
factor = 60

with open('levels/level001.xsb') as f:
    for line in f:
        for zeichen in line:
            
            if zeichen == "@":
                screen.blit(player, (x*factor,y*factor))
                
            if zeichen == "$":
                screen.blit(crate, (x*factor,y*factor))
                
            if zeichen == "#":
                screen.blit(wall, (x*factor,y*factor))
                
            #if zeichen == " ":
            #    screen.blit(ground, (x*factor,y*factor))
                
            if zeichen == ".":
                screen.blit(goal, (x*factor,y*factor))
                    
            x += 1
            
        y += 1
        x = 0
        
    pygame.display.flip()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()