import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, CIRCLE_RADIUS):
        super(Ball, self).__init__()

        self.surface = pygame.Surface((CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, (255, 255, 255, 255), (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)

        self.rect = self.surface.get_rect()
        self.rect.update(SCREEN_WIDTH // 12 + PADDLE_WIDTH, SCREEN_HEIGHT // 2 - CIRCLE_RADIUS, PADDLE_WIDTH, PADDLE_HEIGHT)

    def update(self, state, dir_x, dir_y, speed, angle, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, CIRCLE_RADIUS):
        if state == 0:
            m_loc = pygame.mouse.get_pos()[1]
            if 0 <= m_loc - PADDLE_HEIGHT // 2 <= SCREEN_HEIGHT - PADDLE_HEIGHT:
                self.rect.update(SCREEN_WIDTH // 12 + PADDLE_WIDTH, m_loc - CIRCLE_RADIUS, PADDLE_WIDTH, PADDLE_HEIGHT)
            elif m_loc - PADDLE_HEIGHT // 2 > SCREEN_HEIGHT - PADDLE_HEIGHT:
                self.rect.update(SCREEN_WIDTH // 12 + PADDLE_WIDTH, SCREEN_HEIGHT - PADDLE_HEIGHT // 2 - CIRCLE_RADIUS, PADDLE_WIDTH, PADDLE_HEIGHT)
            else:
                self.rect.update(SCREEN_WIDTH // 12 + PADDLE_WIDTH, PADDLE_HEIGHT // 2 - CIRCLE_RADIUS, PADDLE_WIDTH, PADDLE_HEIGHT)
        
        if state == 1:
            if self.rect.y < 0:
                dir_y = 1

            if self.rect.y + CIRCLE_RADIUS * 2 > SCREEN_HEIGHT:
                dir_y = -1

            self.rect.move_ip(speed * dir_x, speed * dir_y * angle)

            if self.rect.x < SCREEN_WIDTH // 16:
                state = 2

        if state == 2:
            if self.rect.y < 0:
                dir_y = 1

            if self.rect.y + CIRCLE_RADIUS * 2 > SCREEN_HEIGHT:
                dir_y = -1

            if self.rect.x > 0:
                self.rect.move_ip(speed * dir_x, speed * dir_y * angle)

        return state, dir_x, dir_y
