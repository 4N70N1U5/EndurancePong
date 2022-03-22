import pygame


class Ball(pygame.sprite.Sprite):
    CIRCLE_RADIUS = 20

    def __init__(self):
        super(Ball, self).__init__()

        self.surface = pygame.Surface((self.CIRCLE_RADIUS, self.CIRCLE_RADIUS))
        pygame.draw.circle(self.surface, (255, 255, 255), (self.CIRCLE_RADIUS / 2, self.CIRCLE_RADIUS / 2), self.CIRCLE_RADIUS)

        self.rect = self.surface.get_rect()
        self.rect.update()
