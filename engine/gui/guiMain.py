import imgui
import imgui.core
from imgui.integrations.pyglet import PygletFixedPipelineRenderer

from array import array
from math import sin, pi
from random import random
from time import time
from noise import pnoise1

from ..ecs import entity_manager as em
from ..objects.BaseComponents import TransformComponent

C = .01
L = int(pi * 2 * 100)
plot_values = array('f', [sin(x * C) for x in range(L)])
histogram_values = array('f', [random() for x in range(20)])
perlin_values = array('f', [pnoise1(x, x+1) for x in range(20)])


class UI:
    def __init__(self, window, entity_manager):
        """A class to handle ```imgui```
        :param window: A Window from Pyglet
        :type Window
        :param entity_manager: An instance of Entity Manager
        :type EntityManager

        :raises TypeError: when entity_manager is incorrect
        """
        self.entities = []
        self.clicked, self.current = (None, None)
        if not isinstance(entity_manager, em.EntityManager):
            raise TypeError("entity_manager must be an instance of EntityManager")
        self.entity_manager = entity_manager

        imgui.create_context()
        self.renderer = PygletFixedPipelineRenderer(window)
        self.impl = self.renderer

    def render(self):
        imgui.render()
        self.impl.render(imgui.get_draw_data())

    def update(self, isEditor=False):
        imgui.new_frame()
        if isEditor and imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):

                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", '', False, True
                )

                if clicked_quit:
                    exit(1)

                imgui.end_menu()
            if imgui.begin_menu("Test", True):

                clicked_server, selected_server = imgui.menu_item(
                    "Server", '', False, True
                )

                if clicked_server:
                    print("server")

                imgui.end_menu()
            imgui.end_main_menu_bar()

            imgui.begin("Plot example")
            imgui.plot_lines(
                "Sin(t)",
                plot_values,
                overlay_text="SIN() over time",
                # offset by one item every millisecond, plot values
                # buffer its end wraps around
                values_offset=int(time() * 100) % L,
                # 0=auto scale => (0, 50) = (auto scale width, 50px height)
                graph_size=(0, 50),
            )
            imgui.plot_histogram(
                "histogram(random())",
                histogram_values,
                overlay_text="random histogram",
                # offset by one item every millisecond, plot values
                # buffer its end wraps around
                graph_size=(0, 50),
            )
            imgui.plot_histogram(
                "histogram(perlin())",
                perlin_values,
                overlay_text="perlin histogram",
                # offset by one item every millisecond, plot values
                # buffer its end wraps around
                graph_size=(0, 50),
            )
            imgui.end()

            imgui.begin("Entity Debug")
            info_string = f""
            self.clicked, self.current = imgui.listbox(
                f"Entity Info for ${self.current}\n"+info_string, 1, self.entities
            )
            imgui.end()

            imgui.end_frame()

        if self.clicked:
            print(self.current)

        self.entities = []
        for entity in list(self.entity_manager.return_entities()):
            self.entities.append(str(entity.__module__))
