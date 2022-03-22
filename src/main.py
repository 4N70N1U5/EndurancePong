import random
import pygame
from Ball import Ball
from Computer import Computer
from Player import Player


random.seed()

pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_caption('Endurance Pong')
display_info = pygame.display.Info()

SCREEN_WIDTH = display_info.current_w
SCREEN_HEIGHT = display_info.current_h

PADDLE_WIDTH = SCREEN_WIDTH // 40
PADDLE_HEIGHT = SCREEN_HEIGHT // 4
CIRCLE_RADIUS = SCREEN_HEIGHT // 40
FONT_SIZE = SCREEN_WIDTH // 32

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

clock = pygame.time.Clock()

font = pygame.font.Font('./res/Square.ttf', FONT_SIZE)
start = font.render('Press SPACE to start. Press ESC to exit', True, (255, 255, 255))
start_rect = start.get_rect()
start_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
retry = font.render('Press SPACE to retry. Press ESC to exit', True, (255, 255, 255))
retry_rect = retry.get_rect()
retry_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
computer = Computer(SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, CIRCLE_RADIUS)

running = True
state = 0
counter = 0
dir_x = 1
dir_y = 1
speed = 0.3
angle = random.uniform(0.5, 1.5)

score = font.render(str(counter), True, (255, 255, 255))
score_rect = score.get_rect()
score_rect.center = (SCREEN_WIDTH // 2, FONT_SIZE // 2)

while running:
    dt = clock.tick(60)

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and state == 0:
                state = 1
            if event.key == pygame.K_SPACE and state == 2:
                state = 0
                counter = 0
                dir_x = 1
                dir_y = 1
                speed = 0.3
                angle = random.uniform(0.75, 1.25)

    if ball.rect.colliderect(player.rect):
        dir_x = 1
        counter += 1
        speed += 0.02
        angle = random.uniform(0.75, 1.25)
        print(counter)

    if ball.rect.colliderect(computer.rect):
        dir_x = -1
        angle = random.uniform(0.75, 1.25)

    if state == 0:
        window.blit(start, start_rect)

    if state == 2 and ball.rect.x <= 0:
        window.blit(retry, retry_rect)

    score = font.render(str(counter), True, (255, 255, 255))

    player.update(SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
    computer.update(ball, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, CIRCLE_RADIUS)
    state, dir_x, dir_y = ball.update(state, dir_x, dir_y, speed * dt, angle, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, CIRCLE_RADIUS)

    window.blit(score, score_rect)
    window.blit(ball.surface, ball.rect)
    window.blit(player.surface, player.rect)
    window.blit(computer.surface, computer.rect)

    pygame.display.flip()

pygame.quit()
