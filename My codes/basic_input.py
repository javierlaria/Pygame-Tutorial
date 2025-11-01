import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# regular surface blocks
surf = pygame.Surface((50, 50))
surf.fill((0, 0, 0))
rect = surf.get_rect()

surf_center = (
    ((SCREEN_WIDTH - surf.get_width()) / 2),
    ((SCREEN_HEIGHT - surf.get_height()) / 2)
)

# player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((75, 75))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
# player definition
    player = Player()
# input loading
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((255, 255, 255))

    screen.blit(player.surf, surf_center)

    screen.blit(player.surf, player.rect)
    
    pygame.display.flip()

pygame.quit()
