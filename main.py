import pygame
import sys
from game import Game

def main():
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Modern Car Racing')
    clock = pygame.time.Clock()

    def main_menu():
        font = pygame.font.SysFont('Arial', 60)
        small_font = pygame.font.SysFont('Arial', 36)
        while True:
            screen.fill((30, 30, 40))
            title = font.render('Car Racing', True, (255, 215, 0))
            start = small_font.render('1. Start Game', True, (255, 255, 255))
            quit_ = small_font.render('2. Quit', True, (255, 255, 255))
            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 150))
            screen.blit(start, (SCREEN_WIDTH//2 - start.get_width()//2, 300))
            screen.blit(quit_, (SCREEN_WIDTH//2 - quit_.get_width()//2, 360))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return
                    if event.key == pygame.K_2:
                        pygame.quit()
                        sys.exit()
            clock.tick(60)

    main_menu()
    game = Game(screen, clock)
    game.run()

if __name__ == '__main__':
    main()
