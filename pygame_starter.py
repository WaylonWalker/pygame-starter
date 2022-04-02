import pygame


class Game:
    def __init__(self, screen_size=(854, 480), caption="pygame-starter", tick_speed=30):
        pygame.init()
        pygame.display.set_caption(caption)

        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.tick_speed = tick_speed

        self.running = True
        self.surfs = []

    def should_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def game(self):
        ...

    def reset_screen(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        self.should_quit()
        self.reset_screen()
        self.game()
        for surf in self.surfs:
            self.screen.blit(surf, (0, 0))
        pygame.display.update()
        self.clock.tick(self.tick_speed)

    def run(self):
        while self.running:
            self.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
