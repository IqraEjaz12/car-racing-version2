import pygame

class FinishLine:
    def __init__(self, road_x, road_width, track_pos):
        self.x = road_x + 10
        self.width = road_width - 20
        self.height = 20
        self.base_y = track_pos
        self.color = (255, 255, 0)
        self.rect = pygame.Rect(self.x, 0, self.width, self.height)

    def update(self, player_track_pos):
        self.y = 500 - (self.base_y - player_track_pos)
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        if 0 < self.y < screen.get_height():
            pygame.draw.rect(screen, self.color, self.rect)
            # Draw checkered pattern
            for i in range(0, self.width, 20):
                color = (0,0,0) if (i//20)%2==0 else (255,255,255)
                pygame.draw.rect(screen, color, (self.x+i, self.y, 10, self.height))
