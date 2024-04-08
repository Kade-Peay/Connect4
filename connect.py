# use pygame 
# connect 4 game. blue vs. yellow. 7 X 6 grid
# first implement player vs. player, then player vs computer 

import pygame
import numpy as np  
import player

# initialize pygame and get window showing 
pygame.init()
back = (192,192,192)

# image for board background 
boardImage = pygame.image.load("Connect4Board.png")

# set up data for the board 
board = np.full((7,6), 0)
print(board)

gameWindow = pygame.display.set_mode((640,480))
pygame.display.set_caption('Connect 4')
gameWindow.fill(back)
clock = pygame.time.Clock()

# Set up players 
player1 = player.Player("red")
player2 = player.Player("yellow")

print(player2.color)

running = True 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Load 'or blit I guess?' the background png 
    gameWindow.blit(boardImage, (0,0))

    # Check for click. On click, check which player for color, paste at position 


    # Upadte stuff every clock tick 
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()