import pygame


class Computer(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT):
        super(Computer, self).__init__()

        self.surface = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.surface.fill((255, 255, 255))

        self.rect = self.surface.get_rect()
        self.rect.update(SCREEN_WIDTH - SCREEN_WIDTH // 12 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    def update(self, ball, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, CIRCLE_RADIUS):
        b_loc = ball.rect.y + CIRCLE_RADIUS
        if 0 <= b_loc - PADDLE_HEIGHT // 2 <= SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.update(SCREEN_WIDTH - SCREEN_WIDTH // 12 - PADDLE_WIDTH, b_loc - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        elif b_loc - PADDLE_HEIGHT // 2 > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.update(SCREEN_WIDTH - SCREEN_WIDTH // 12 - PADDLE_WIDTH, SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
        else:
            self.rect.update(SCREEN_WIDTH - SCREEN_WIDTH // 12 - PADDLE_WIDTH, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
