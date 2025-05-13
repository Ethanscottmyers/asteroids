import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), (pygame.SRCALPHA))
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt, screen):
        self.position += self.velocity * dt
        self.rect.center = self.position
        self.draw(screen)
