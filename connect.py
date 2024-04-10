# use pygame 
# connect 4 game. blue vs. yellow. 7 X 6 grid
# first implement player vs. player, then player vs computer 

import pygame
import numpy as np  
import player

# initialize pygame and get window showing 
pygame.init()
back = (192,192,192)

width, height = 640, 480
gameWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption('Connect 4')
gameWindow.fill(back)
clock = pygame.time.Clock()

# image for board background 
boardImage = pygame.image.load("Connect4Board.png")

# set up data for the board. 7 across, 6 down, set as 0 
rows, cols = 6, 7 # Declaring as variables so I can use them for other stuff. Public variables are sick
board = np.full((rows, cols), 0)


# for drawing the circle later
radius = 38
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
            updateArray(col, playerTurn)


            # I know this is an incredibly crude way to keep track of which players turn it is and actual players but it kinda works so
            if playerTurn == 1:
                playerTurn = 2
            else:
                playerTurn = 1

            updateBoard()
            check = check_victory(board)
            if check != 0:
                print(f"Player {check} is the winner")

    # called on click, update the array based on player
    def updateArray(col, playerTurn):
        for row in reversed(range(rows)):
            if board[int(row)][int(col)] == 0:
                board[int(row)][int(col)] = playerTurn
                return
            

    # update the drawn board. basically just loop through and draw the entire array after every click. 
    # I know I could probably only draw the updates but I don't care to
    def updateBoard():
        # Later
        for row in range(rows):
            for col in range(cols):
                center_x = int((col + .5) * spacing_x)
                center_y = int((row + .5) * spacing_y)
                if board[row][col] == 1:
                    pygame.draw.circle(gameWindow, player1, (center_x, center_y), radius)
                if board[row][col] == 2:
                    pygame.draw.circle(gameWindow, player2, (center_x, center_y), radius)


    # https://stackoverflow.com/questions/74692439/how-do-i-check-for-a-4-in-a-row-with-a-2d-array-note-that-im-not-using-nump
    # Had to change the initial 2 for loops to -3 instead of 4. I didn't change anything else but otherwise the win condition was at 5 in a row
    def check_victory(board: np.array) -> int:
        """
        Navigating through all 4x4 subfields and check for victory condition
        of either player. 
        :returns: 1 or 2 of player 1 or 2 has won, 0 otherwise.
        """
        for row in range(rows - 3):
            for col in range(cols - 3):
                v = check_subfield(board[row:row + 4, col:col + 4])
                if v > 0:
                    return v
        return 0


    def check_subfield(field: np.array) -> int:
        # check diagonal.
        v = same_number(np.diagonal(field))
        if v > 0:
            return v
        for i in range(4):
            # check column
            v = same_number(field[i, :])
            if v > 0:
                return v
            # check row
            v = same_number(field[:, i])
            if v > 0:
                return v
        return 0

    def same_number(values: list) -> int:
        return int((values == values[0]).all() * values[0])


    # Check rows
    def checkHorizontal():
        pass

    # Check cols
    def checkVertical():
        pass

    # Check across both horizontal and diagonal
    def checkDiagonal():
        pass

    # Load 'or blit I guess?' the background png 
    gameWindow.blit(boardImage, (0,0))
    # Upadte stuff every clock tick 
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()