from pygame_starter import Game


class MyGame(Game):
    def game(self):
        self.screen.fill((128, 255, 255))


if __name__ == "__main__":
    game = MyGame()
    game.run()
