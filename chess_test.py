import pygame
import chess

pygame.init()

gameDisplay = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Chess Deep Neural Network')

clock = pygame.time.Clock()
board = chess.Board()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    pygame.display.Info()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
