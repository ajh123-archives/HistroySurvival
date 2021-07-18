from ..constants import *
from .Scene import Scene
from ..ecs import entity_manager as em
from ..objects import BaseComponents as bC
from ..objects import BaseSystems as bS
from ..gui import guiMain
import time


# IntoScreen is a class that inherits a background, the background is Spr (our custom background-image class)
# IntoScreen contains 1 label, and it will change it's text after 2 seconds of being shown.
# That's all it does.
class GameScreen(Scene):
    def __init__(self, game, texture=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, x=0, y=0, color='#000000'):
        super(GameScreen, self).__init__(game, texture, width=width, height=height, x=x, y=y, color=color)
        self.has_been_visible_since = time.time()

        self.entity_manager = em.EntityManager()
        self.gui = guiMain.UI(self.game, self.entity_manager)

        self.camera = em.Entity()
        self.banana = em.Entity()
        self.entity_manager.add_entity(self.camera)
        self.entity_manager.add_entity(self.banana)
        self.entity_manager.add_component_to_entity(self.camera, bC.TransformComponent())
        self.entity_manager.add_component_to_entity(self.banana, bC.TransformComponent())

        self.moveSystem = bS.MovementSystem(self.entity_manager)
        self.entity_manager.add_system(self.moveSystem)

    def draw_(self, game):
        self.draw()
        self.gui.render()

    def update_(self, delta_time):
        self.entity_manager.update(delta_time)
        self.gui.update()
