import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # prepare FPS limitation to 60
    time = pygame.time.Clock()
    time_delta = 0

    # prepare update groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    # prepare the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # spawn in middle of window

    # prepare asteroids
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update screen
        screen.fill("black")

        # update stuff
        for object in updateable:
            object.update(time_delta)

        # analyse collisions
        for asteroid in asteroids:
            # handle player collision
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            # handle bullet collision
            for shot in shots:
                if shot.collides_with(asteroid):
                    shot.kill() # pygame function to remove object
                    asteroid.split()

        # draw stuff
        for object in drawable:
            object.draw(screen)

        # update content on screen and time
        pygame.display.flip()
        time_delta = time.tick(60) / 1000

if __name__ == "__main__":
    main()
