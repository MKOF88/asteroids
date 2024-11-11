import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()

        # handle small asteroid which are getting destroyed (no split)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # split asteroid - preparation
        random_angle = random.uniform(20, 50) # random number between 20 and 50
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # split asteroids
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_velocity = self.velocity.rotate(random_angle)
        new_asteroid.velocity = new_velocity * 1.2

        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_velocity = self.velocity.rotate(-random_angle)
        new_asteroid.velocity = new_velocity * 1.2
