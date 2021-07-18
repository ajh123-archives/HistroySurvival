import pyglet
from time import time
from .constants import *
from .scenes.IntroScene import IntroScreen
from .scenes.MenuScene import MenuScreen
from .scenes.GameScene import GameScreen
from .scenes.EditorScene import EditorScreen


# This is the actual window, the game, the glory universe that is graphics.
# It will be blank, so you need to set up what should be visible when and where.
# I've created two classes which can act as "screens" (intro, game, menu etc)
# And we'll initiate the Window class with the IntroScreen() and show that for a
# total of 5 seconds, after 5 seconds we will swap it out for a MenuScreen().
# All this magic is done in __init__() and render(). All the other functions are basically
# just "there" and executes black magic for your convenience.
class PygletWindow(pyglet.window.Window):
    def __init__(self, refreshRate):
        super(PygletWindow, self).__init__(vsync=False,
                                           width=WINDOW_WIDTH,
                                           height=WINDOW_HEIGHT,
                                           caption='History Survival',
                                           resizable=True
                                           )

        self.alive = 1
        self.refreshRate = refreshRate

        self.currentScreen = IntroScreen(self, x=1, y=1, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # <-- Important
        self.screen_has_been_shown_since = time()
        self.hasLoaded = False

        pyglet.clock.schedule_interval(self.update, 1.0 / refreshRate)

    def on_draw(self):
        self.render()

    def update(self, delta_time):
        self.currentScreen.update_(delta_time)

    def render(self):
        self.clear()
        if time() - 5 > self.screen_has_been_shown_since and type(self.currentScreen) is not MenuScreen:  # <- Important
            if type(self.currentScreen) is GameScreen:
                pass
            else:
                self.currentScreen = MenuScreen(self,
                                                x=WINDOW_WIDTH/2,
                                                y=WINDOW_HEIGHT/2,
                                                width=WINDOW_WIDTH,
                                                height=WINDOW_HEIGHT,
                                                color='#AA0000'
                                                )  # <-- Important, here we switch screen (after 5 seconds)

        self.currentScreen.draw_(self)  # <-- Important, draws the current screen

    def on_close(self):
        self.alive = 0

    def on_mouse_press(self, x, y, button, modifiers):
        self.currentScreen.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.currentScreen.on_mouse_motion(x, y, delta_x, delta_y)

    def on_key_press(self, key, modifiers):
        self.currentScreen.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.currentScreen.on_key_release(key, modifiers)

    def set_scene(self, scene):
        self.currentScreen = scene


class EditPygletWindow(PygletWindow):
    def __init__(self, refreshRate):
        super(EditPygletWindow, self).__init__(refreshRate)
        self.currentScreen = EditorScreen(self, x=1, y=1, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    def render(self):
        self.clear()
        self.currentScreen.draw_(self)
