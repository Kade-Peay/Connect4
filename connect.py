# use pygame 
# connect 4 game. blue vs. yellow. 7 X 6 grid
# first implement player vs. player, then player vs computer 

import pygame
import numpy as np  
import player

# initialize pygame and get window showing 
pygame.init()
back = (192,192,192)

# for drawing the circle later
radius = 38

# image for board background 
boardImage = pygame.image.load("Connect4Board.png")

# set up data for the board. 7 across, 6 down, set as 0 
rows, cols = 6, 7 # it seems silly to do this now but I use it later
board = np.full((rows, cols), 0)

width, height = 640, 480
gameWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 4')
gameWindow.fill(back)
clock = pygame.time.Clock()

spacing_x = width / cols
spacing_y = height / rows

# These used to be made using an object but that may be phased out later
# Set up players. red will equal 1, yellow 2 in the board array 
player1 = "red"
player2 = "yellow"
playerTurn = 1


running = True 
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check for click. On click, check which player for color, paste at position 
        if event.type == pygame.MOUSEBUTTONDOWN:
            # When checking for position, only check x-direction. y-axis is unnceessary because it fills bottom to top
            x = pygame.mouse.get_pos()[0]

            # column clicked
            col = x // spacing_x

            # center of that column 
            center_x = (col + .5) * spacing_x

            # Call function that returns which row in the col to put the circle.
            y = boardUpdate(col, playerTurn)
            
            row = y // spacing_y
            center_y = (row + .5) * spacing_y


            # I know this is an incredibly crude way to keep track of which players turn it is and actual players but it kinda works so
            if playerTurn == 1:
                current_player = player1
                playerTurn = 2
            else:
                current_player = player2
                playerTurn = 1

            # Actual draw of the circle
            pygame.draw.circle(gameWindow, current_player, (center_x, center_y), radius)


    def boardUpdate(col, playerTurn):
        for row in range(rows):
            if row == 0:
                board[int(row)][int(col)] = playerTurn
                print(board)
                return row


    def centerCircles():
        # Later
        for row in range(rows):
            for col in range(cols):
                center_x = int((col + .5) * spacing_x)
                center_y = int((row + .5) * spacing_y)
                pygame.draw.circle(gameWindow, "blue", (center_x, center_y), 5)

    # Load 'or blit I guess?' the background png 
    gameWindow.blit(boardImage, (0,0))
    # Upadte stuff every clock tick 
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()