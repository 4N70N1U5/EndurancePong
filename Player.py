import pygame


class Player(pygame.sprite.Sprite):
    RECT_WIDTH = 25
    RECT_HEIGHT = 100
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super(Player, self).__init__()

        self.surface = pygame.Surface((self.RECT_WIDTH, self.RECT_HEIGHT))
        self.surface.fill((255, 255, 255))

        self.rect = self.surface.get_rect()
        self.rect.update(SCREEN_WIDTH / 9, SCREEN_HEIGHT / 2 - self.RECT_HEIGHT / 2, self.RECT_WIDTH, self.RECT_HEIGHT)
    
    def update(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        m_loc = pygame.mouse.get_pos()[1]
        if 0 <= m_loc - self.RECT_HEIGHT / 2 <= SCREEN_HEIGHT - self.RECT_HEIGHT:
            self.rect.update(SCREEN_WIDTH / 9, m_loc - self.RECT_HEIGHT / 2, self.RECT_WIDTH, self.RECT_HEIGHT)
        elif m_loc - self.RECT_HEIGHT / 2 > SCREEN_HEIGHT - self.RECT_HEIGHT:
            self.rect.update(SCREEN_WIDTH / 9, SCREEN_HEIGHT - self.RECT_HEIGHT, self.RECT_WIDTH, self.RECT_HEIGHT)
        else:
            self.rect.update(SCREEN_WIDTH / 9, 0, self.RECT_WIDTH, self.RECT_HEIGHT)
