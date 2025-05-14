import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), (pygame.SRCALPHA))
        self.rect = self.image.get_rect(center=(x, y))


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_child1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_child1.velocity = new_vector1 * 1.2
            new_child2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_child2.velocity = new_vector2 * 1.2


    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt, screen):
        self.position += self.velocity * dt
        self.rect.center = self.position
        self.draw(screen)
