from ..constants import *
from .Scene import Scene
import pyglet
import time


# IntoScreen is a class that inherits a background, the background is Spr (our custom background-image class)
# IntoScreen contains 1 label, and it will change it's text after 2 seconds of being shown.
# That's all it does.
class IntroScreen(Scene):
    def __init__(self, game, texture=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, x=0, y=0, color='#000000'):
        super(IntroScreen, self).__init__(game, texture, width=width, height=height, x=x, y=y, color=color)

        self.intro_text = pyglet.text.Label('Starting History Survival',
                                            font_size=10,
                                            font_name=('Verdana', 'Calibri', 'Arial'),
                                            x=int(width/2),
                                            y=int(height/2),
                                            multiline=False,
                                            width=int(width/2),
                                            height=int(height/2),
                                            color=(100, 100, 100, 255),
                                            anchor_x='center')
        self.has_been_visible_since = time.time()

    def draw_(self, game):  # <-- Important, this is the function that is called from the main window.render()
        # function. The built-in rendering function of pyglet is called .draw() so we create a manual one that's
        # called _draw() that in turn does stuff + calls draw(). This is just so we can add on to the functionality
        # of Pyglet.
        self.draw()
        self.intro_text.draw()
        if time.time() - 2 > self.has_been_visible_since:
            self.intro_text.text = 'ajh-123 development'
