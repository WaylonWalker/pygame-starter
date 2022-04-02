from typing import Tuple

import pygame


class Game:
    def __init__(
        self,
        screen_size: Tuple[int, int] = (854, 480),
        caption: str = "pygame-starter",
        tick_speed: int = 60,
    ):
        """

        screen_size (Tuple[int, int]): The size of the screen you want to use, defaults to 480p.
        caption (str): the name of the game that will appear in the title of the window, defaults to `pygame-starter`.
        tick_speed (int): the ideal clock speed of the game, defaults to 60

        ## Example Game

        You can make a quick game by inheriting from Game, and calling
        `.run()`.  This example just fills the screen with an aqua color, but
        you can put all of your game logic in the `game` method.

        ``` python
        from pygame_starer import Game

        class MyGame(Game):
            def game(self):
                self.screen.fill((128, 255, 255))

        if __name__ == "__main__":
            game = MyGame()
            game.run()

        ```
        """
        pygame.init()
        pygame.display.set_caption(caption)

        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.tick_speed = tick_speed

        self.running = True
        self.surfs = []

    def should_quit(self):
        """check for pygame.QUIT event and exit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def game(self):
        """
        This is where you put your game logic.

        """
        ...

    def reset_screen(self):
        """
        fill the screen with black
        """
        self.screen.fill((0, 0, 0))

    def update(self):
        """
        run one update cycle
        """
        self.should_quit()
        self.reset_screen()
        self.game()
        for surf in self.surfs:
            self.screen.blit(surf, (0, 0))
        pygame.display.update()
        self.clock.tick(self.tick_speed)

    def run(self):
        """
        run update at the specified tick_speed, until exit.
        """
        while self.running:
            self.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
