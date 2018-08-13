import pygame, arena, gameover
from Menu import menu

pygame.init()

width = 1024
height = 576

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('game')

gameState = 'menu'

while not gameState == 'quit':
    if gameState == 'menu':
        gameState = menu.loop(window)

    if gameState == 'arena':
        gameState = arena.loop(window)

    if gameState == 'gameover':
        gameState = gameover.loop(window)

pygame.quit()
quit()