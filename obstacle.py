import pygame
import random

class Obstacle:
    def __init__(self, road_x, road_width, track_pos):
        self.width = 50
        self.height = 50
        self.color = (200, 50, 50)
        self.x = random.randint(road_x + 10, road_x + road_width - self.width - 10)
        self.base_y = random.randint(300, 2000)  # Distance along the track
        self.track_pos = track_pos
        self.rect = pygame.Rect(self.x, 0, self.width, self.height)

    def update(self, player_track_pos):
        # Calculate screen y relative to player
        self.y = 500 - (self.base_y - player_track_pos)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if 0 < self.y < screen.get_height():
            pygame.draw.rect(screen, self.color, self.rect)
