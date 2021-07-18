from ..ecs.iterator_system import IteratorSystem
from ..objects.BaseComponents import TransformComponent


class MovementSystem(IteratorSystem):
    def __init__(self, entity_manager):
        super().__init__()
        # Get the Family of entities with position and velocity components:
        self.family = entity_manager.get_family(TransformComponent)
        # Get the component maps so we can access the components using the entity as a key:
        self.transform_component_map = entity_manager.get_component_map(TransformComponent)

    def process(self, deltaTime, entity):
        transform_component_map = self.transform_component_map[entity]
        transform_component_map.x += transform_component_map.vx * deltaTime
        transform_component_map.y += transform_component_map.vy * deltaTime
        transform_component_map.z += transform_component_map.vz * deltaTime
