from ..constants import *
from .Scene import Scene
from .GameScene import GameScreen
import pyglet


# Then we have a MenuScreen (with a red background)
# Note that the RED color comes not from this class because the default is black #000000
# the color is set when calling/instancing this class further down.
# But all this does, is show a "menu" (aka a text saying it's the menu..)
class MenuScreen(Scene):
    def __init__(self, game, texture=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, x=0, y=0, color='#000000'):
        super(MenuScreen, self).__init__(game, texture, width=width, height=height, x=x, y=y, color=color)

        self.screen_text = pyglet.text.Label('Main menu screen',
                                             font_size=40,
                                             font_name=('Verdana', 'Calibri', 'Arial'),
                                             x=x,
                                             y=height-40,
                                             multiline=False,
                                             width=width,
                                             height=height,
                                             color=(100, 100, 100, 255),
                                             anchor_x='center'
                                             )

    def draw_(self, game):
        self.draw()
        self.screen_text.draw()

    def update_(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.E:
            print(True)
            self.game.set_scene(GameScreen(self.game))
