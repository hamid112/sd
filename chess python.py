import pygame
pygame.init()

#set display
gameDisplay = pygame.display.set_mode((800,600))

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('chess project')

#caption
pygame.display.set_caption("ChessBoard")

#load images
background = pygame.image.load('acual project game.png')

#beginning of logic
gameExit = False

#For loop for chessboard
while not gameExit:

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        
#For loop for chessboard






















#quit from pygame and python
pygame.quit()
quit()
