import pygame
from Computer import Computer

from Player import Player


pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576

PADDLE_WIDTH = 25
PADDLE_HEIGHT = 100

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
computer = Computer(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    player.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    computer.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    window.blit(player.surface, player.rect)
    window.blit(computer.surface, computer.rect)

    pygame.display.flip()

pygame.quit()
