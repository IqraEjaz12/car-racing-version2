
import pygame
import random
from player import PlayerCar
from ai import AICar
from track import Track



from obstacle import Obstacle
from finish_line import FinishLine

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.track = Track(screen.get_width(), screen.get_height())
        # Cars start in the center of the road
        road_x = (screen.get_width() - 400) // 2
        self.road_x = road_x
        self.road_width = 400
        self.player = PlayerCar(road_x + 80, 500)
        self.ai = AICar(road_x + 220, 500)
        # Add more obstacles for a real racing challenge
        self.obstacles = [Obstacle(self.road_x, self.road_width, random.randint(400, 4000)) for _ in range(15)]
        # Lap and finish line
        self.lap_length = 2000
        self.laps = 0
        self.finish_line = FinishLine(self.road_x, self.road_width, self.lap_length)
        self.crossed = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update player (updates track_pos)
            self.player.update()

            # Make the road scroll only when the car reaches the middle of the screen
            scroll_zone = 300
            if self.player.y < scroll_zone:
                scroll_amount = scroll_zone - self.player.y
                self.player.y = scroll_zone
                self.player.track_pos += scroll_amount
                # Move obstacles and finish line down by scroll_amount
                for obs in self.obstacles:
                    obs.base_y += scroll_amount
                self.finish_line.base_y += scroll_amount

            # Update track rendering based on player's progress
            self.track.update(self.player.track_pos)

            # Draw track
            self.track.draw(self.screen)

            # Update and draw finish line
            self.finish_line.update(self.player.track_pos)
            self.finish_line.draw(self.screen)

            # Lap logic
            if self.player.track_pos >= self.lap_length and not self.crossed:
                if self.player.rect.colliderect(self.finish_line.rect):
                    self.laps += 1
                    self.crossed = True
            if self.player.track_pos < self.lap_length:
                self.crossed = False

            # Update and draw obstacles
            for obs in self.obstacles:
                obs.update(self.player.track_pos)
                obs.draw(self.screen)
                # Collision detection
                if self.player.rect.colliderect(obs.rect):
                    # Simple effect: reset player position
                    self.player.x = self.road_x + 80
                    self.player.y = 500
                    self.player.track_pos = 0

            # Update AI car (relative to player, avoid obstacles)
            self.ai.update(self.player.track_pos, self.obstacles)

            # Draw cars
            self.player.draw(self.screen)
            self.ai.draw(self.screen)

            # Draw lap count and speed
            font = pygame.font.SysFont('Arial', 32)
            lap_text = font.render(f'Laps: {self.laps}', True, (255,255,255))
            self.screen.blit(lap_text, (20, 20))
            speed_text = font.render(f'Speed: {abs(self.player.track_pos) // 10}', True, (255,255,255))
            self.screen.blit(speed_text, (20, 60))

            pygame.display.flip()
            self.clock.tick(60)
