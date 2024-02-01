import pygame, sys
#from namoradinha import Amor_da_minha_vida
#from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen.fill('White')
        pygame.display.set_caption('Crazy Love')
        self.clock = pygame.time.Clock()
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick() / 1000
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()