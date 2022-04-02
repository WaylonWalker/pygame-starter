# pygame-starter

## Installation

``` bash
pip install git+https://github.com/WaylonWalker/pygame-starter
```

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
