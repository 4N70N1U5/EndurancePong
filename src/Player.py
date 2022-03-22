import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT):
        super(Player, self).__init__()

        self.surface = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.surface.fill((255, 255, 255))

        self.rect = self.surface.get_rect()
        self.rect.update(SCREEN_WIDTH // 12, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    def update(self, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT):
        m_loc = pygame.mouse.get_pos()[1]
        if 0 <= m_loc - PADDLE_HEIGHT // 2 <= SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.update(SCREEN_WIDTH // 12, m_loc - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
        elif m_loc - PADDLE_HEIGHT // 2 > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.rect.update(SCREEN_WIDTH // 12, SCREEN_HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
        else:
            self.rect.update(SCREEN_WIDTH // 12, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
