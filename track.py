import pygame

class Track:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bg_color = (40, 120, 40)
        self.road_color = (60, 60, 60)
        self.line_color = (255, 255, 255)
        self.road_width = 400
        self.line_height = 40
        self.line_gap = 40

    def update(self, player_track_pos):
        self.player_track_pos = player_track_pos

    def draw(self, screen):
        screen.fill(self.bg_color)
        road_x = (self.width - self.road_width) // 2
        # Draw road
        pygame.draw.rect(screen, self.road_color, (road_x, 0, self.road_width, self.height))
        # Draw road edges
        edge_color = (220, 220, 220)
        edge_width = 8
        pygame.draw.rect(screen, edge_color, (road_x, 0, edge_width, self.height))
        pygame.draw.rect(screen, edge_color, (road_x + self.road_width - edge_width, 0, edge_width, self.height))
        # Draw lane lines (3 lanes)
        lane_color = (180, 180, 180)
        lane_width = 4
        for i in range(1, 3):
            lane_x = road_x + i * self.road_width // 3
            pygame.draw.line(screen, lane_color, (lane_x, 0), (lane_x, self.height), lane_width)
        # Draw dashed center line, always relative to player's track position
        offset = self.player_track_pos % (self.line_height + self.line_gap)
        y = -offset
        for i in range(3):
            line_x = road_x + (i + 0.5) * self.road_width // 3 - 5
            y = -offset
            while y < self.height:
                pygame.draw.rect(screen, self.line_color, (line_x, y, 10, self.line_height))
                y += self.line_height + self.line_gap
