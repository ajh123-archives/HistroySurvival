import imgui
import imgui.core


class Entity:
    """Simple Universally Unique Identifiers (UUIDs) used to identify this Entity in the Entity Manager."""
    def __init__(self):
        pass

    def render_debug(self, entity_manager):
        components = entity_manager.get_entity_components(self)
        for component in components:
            self.create_component_debug(component)

    @staticmethod
    def create_component_debug(component):
        if imgui.tree_node(str(type(component).__name__), imgui.TREE_NODE_DEFAULT_OPEN):
            for key, value in component.__dict__.items():
                imgui.text(key+" : "+str(value))
            imgui.tree_pop()
