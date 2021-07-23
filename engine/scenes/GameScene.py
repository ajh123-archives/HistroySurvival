import math
import time

from pyglet.gl import *

from .Scene import Scene
from ..constants import *
from ..ecs import entity_manager as em
from ..ecs import entity as en
from ..objects import BaseComponents as bC
from ..objects import BaseSystems as bS
from ..gui import guiMain


# IntoScreen is a class that inherits a background, the background is Spr (our custom background-image class)
# IntoScreen contains 1 label, and it will change it's text after 2 seconds of being shown.
# That's all it does.
class GameScreen(Scene):
    def __init__(self, game, texture=None, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, x=0, y=0, color='#000000'):
        super(GameScreen, self).__init__(game, texture, width=width, height=height, x=x, y=y, color=color)
        self.has_been_visible_since = time.time()

        self.entity_manager = em.EntityManager()
        self.gui = guiMain.UI(self.game, self.entity_manager)

        self.camera = en.Entity()
        self.entity_manager.add_entity(self.camera)
        self.entity_manager.add_component_to_entity(self.camera, bC.TransformComponent())

        self.moveSystem = bS.MovementSystem(self.entity_manager)
        self.renderSystem = None
        self.entity_manager.add_system(self.moveSystem)

        self.isFirstDraw = True

    def draw_(self, game):
        if self.isFirstDraw:
            self.renderSystem = bS.RenderSystem(self.entity_manager, self)
            self.entity_manager.add_system(self.renderSystem)
            self.isFirstDraw = False
        self.draw()
        self.set_3d()
        for entity in list(self.entity_manager.return_entities()):
            self.renderSystem.render(entity)
        self.set_2d()
        self.gui.render()

    def update_(self, delta_time):
        self.entity_manager.update(delta_time)
        self.gui.update()

    def set_2d(self):
        """ Configure OpenGL to draw in 2d.
        """
        width, height = self.game.get_size()
        glDisable(GL_DEPTH_TEST)
        viewport = self.game.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, max(1, width), 0, max(1, height), -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def set_3d(self):
        """ Configure OpenGL to draw in 3d.
        """
        width, height = self.game.get_size()
        glEnable(GL_DEPTH_TEST)
        viewport = self.game.get_viewport_size()
        glViewport(0, 0, max(1, viewport[0]), max(1, viewport[1]))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, width / float(height), 0.1, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        transform = list(self.entity_manager.get_entity_components(self.camera))[0]
        glRotatef(transform.rotation_x, 0, 1, 0)
        glRotatef(-transform.rotation_y,
                  math.cos(math.radians(transform.rotation_x)),
                  0,
                  math.sin(math.radians(transform.rotation_x))
                  )
        glTranslatef(-transform.x, -transform.y, -transform.z)
