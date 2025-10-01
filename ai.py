import pygame
import random
import os

class AICar:
    def __init__(self, x, y):
        self.base_x = x
        self.base_y = y
        self.width = 50
        self.height = 90
        self.speed = 6
        self.track_pos = 0  # AI's progress along the track
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = None
        self.use_rect = False
        try:
            if os.path.exists('assets/car_red.png'):
                img = pygame.image.load('assets/car_red.png')
                self.image = pygame.transform.scale(img, (self.width, self.height))
            else:
                self.use_rect = True
        except Exception:
            self.use_rect = True

    def update(self, player_track_pos, obstacles=None):
        # AI moves forward, slight random left/right
        self.track_pos += self.speed
        # Simple AI: avoid obstacles if provided
        if obstacles:
            for obs in obstacles:
                obs_y = self.base_y - (obs.base_y - self.track_pos)
                if abs(obs_y - self.base_y) < 100 and abs(obs.x - self.base_x) < 60:
                    # Try to dodge
                    if self.base_x < 500:
                        self.base_x += 10
                    else:
                        self.base_x -= 10
        if random.random() < 0.02:
            self.base_x += random.choice([-5, 0, 5])
        # Calculate screen y relative to player
        self.x = self.base_x
        self.y = self.base_y - (self.track_pos - player_track_pos)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.image and not self.use_rect:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, (255, 80, 80), self.rect)
