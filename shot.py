import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), (pygame.SRCALPHA))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt, screen):
        self.position += self.velocity * dt
        self.rect.center = self.position
        self.draw(screen)