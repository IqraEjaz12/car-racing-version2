import pygame
import os

class PlayerCar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 90
        self.speed = 0
        self.max_speed = 8
        self.acceleration = 0.3
        self.track_pos = 0  # Player's progress along the track
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = None
        self.use_rect = False
        try:
            if os.path.exists('assets/car_blue.png'):
                img = pygame.image.load('assets/car_blue.png')
                self.image = pygame.transform.scale(img, (self.width, self.height))
            else:
                self.use_rect = True
        except Exception:
            self.use_rect = True

    def update(self):
        keys = pygame.key.get_pressed()
        move_x, move_y = 0, 0
        if keys[pygame.K_UP]:
            move_y = -6
        if keys[pygame.K_DOWN]:
            move_y = 6
        if keys[pygame.K_LEFT]:
            move_x = -6
        if keys[pygame.K_RIGHT]:
            move_x = 6
        self.x += move_x
        self.y += move_y
        # Clamp to screen bounds (optional, can be improved for road bounds)
        self.x = max(0, min(self.x, 1000 - self.width))
        self.y = max(0, min(self.y, 700 - self.height))
        # Track position is based on upward movement
        if move_y < 0:
            self.track_pos += abs(move_y)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.image and not self.use_rect:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, (0, 200, 255), self.rect)
