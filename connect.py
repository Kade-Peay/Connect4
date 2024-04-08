# use pygame 
# connect 4 game. blue vs. yellow. 7 X 6 grid
# first implement player vs. player, then player vs computer 

import pygame 

# initialize pygame and get window showing 
pygame.init()
back = (192,192,192)
gameWindow = pygame.display.set_mode((800,700))
pygame.display.set_caption('Connect 4')
gameWindow.fill(back)
clock = pygame.time.Clock()
running = True 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()