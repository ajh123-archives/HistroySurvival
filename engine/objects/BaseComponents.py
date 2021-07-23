from ..ecs import component
import pywavefront


class TransformComponent(component.Component):
    def __init__(self):
        self.x = 1
        self.y = 4
        self.z = 8
        self.velocity_x = 0  # 1
        self.velocity_y = 0  # 4
        self.velocity_z = 0  # 8
        self.rotation_x = 0
        self.rotation_y = 0
        self.rotation_z = 0


class MeshRendererComponent(component.Component):
    def __init__(self,  mesh):
        if not isinstance(mesh, pywavefront.Wavefront):
            raise TypeError("mesh needs to be an instance of pywavefront.Wavefront")
        self.mesh = mesh
