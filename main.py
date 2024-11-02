import pygame

from constants import *
from player import Player


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

    Player.containers = (updateable, drawable) 

    # prepare the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # spawn in middle of window
    player2 = Player(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2) # spawn in middle of window



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update screen
        screen.fill("black")

        # update stuff
        for object in updateable:
            object.update(time_delta)

        # draw stuff
        for object in drawable:
            object.draw(screen)

        # update content on screen and time
        pygame.display.flip()
        time_delta = time.tick(60) / 1000

if __name__ == "__main__":
    main()
