from ..constants import *
from ..scenes.GameScene import GameScreen


class EditorScreen(GameScreen):
    def __init__(self, game, texture=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, x=0, y=0, color='#000000'):
        super(EditorScreen, self).__init__(game, texture, width=width, height=height, x=x, y=y, color=color)

    def update_(self, delta_time):
        self.entity_manager.update(delta_time)
        self.gui.update(isEditor=True)
