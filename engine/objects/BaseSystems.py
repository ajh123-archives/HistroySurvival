from ..ecs.iterator_system import IteratorSystem
from ..objects.BaseComponents import TransformComponent
from ..objects.BaseComponents import MeshRendererComponent
from pywavefront import visualization


class MovementSystem(IteratorSystem):
    def __init__(self, entity_manager):
        super().__init__()
        # Get the Family of entities with position and velocity components:
        self.family = entity_manager.get_family(TransformComponent)
        # Get the component maps so we can access the components using the entity as a key:
        self.transform_component_map = entity_manager.get_component_map(TransformComponent)

    def process(self, deltaTime, entity):
        transform_component_map = self.transform_component_map[entity]
        transform_component_map.x += transform_component_map.velocity_x * deltaTime
        transform_component_map.y += transform_component_map.velocity_y * deltaTime
        transform_component_map.z += transform_component_map.velocity_z * deltaTime


class RenderSystem(IteratorSystem):
    def __init__(self, entity_manager, game):
        super().__init__()
        # Get the Family of entities with position and velocity components:
        self.family = entity_manager.get_family(MeshRendererComponent)
        # Get the component maps so we can access the components using the entity as a key:
        self.mesh_component_map = entity_manager.get_component_map(MeshRendererComponent)
        self.game = game

    def process(self, deltaTime, entity):
        pass

    def render(self, entity):
        if entity and self.mesh_component_map:
            try:
                mesh_component_map = self.mesh_component_map[entity]
                visualization.draw(mesh_component_map.mesh)
            except KeyError:
                pass
