import pyglet
from ..constants import *


class Scene(pyglet.sprite.Sprite):
    def __init__(self, game, texture=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, color='#000000', x=0, y=0):
        self.game = game
        if texture is None:
            self.texture = pyglet.image.SolidColorImagePattern(hex_to_rgba_colour(color)).create_image(width,
                                                                                                       height)
        else:
            self.texture = texture
        super(Scene, self).__init__(self.texture)

        # Normally, objects in graphics have their anchor in the bottom left corner.
        # This means that all X and Y coordinates relate to the bottom left corner of
        # your object as positioned from the bottom left corner of your application-screen.
        # We can override this and move the anchor to the WIDTH/2 (aka center of the image).
        # And since Spr is a class only meant for generating a background-image to your "intro screen" etc
        # This only affects this class aka the background, so the background gets positioned by it's center.
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2

        # And this sets the position.
        self.x = x
        self.y = y

    def draw_(self, game):
        self.draw()
        self.clear()

    def update_(self, delta_time):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

