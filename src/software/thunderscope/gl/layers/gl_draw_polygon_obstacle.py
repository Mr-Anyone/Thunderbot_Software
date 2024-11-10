from software.thunderscope.binary_context_managers.full_system import ProtoUnixIO
from software.thunderscope.gl.graphics.gl_polygon import GLPolygon
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.Qt.QtCore import Qt
from pyqtgraph.opengl import *

from proto.import_all_protos import *
from software.py_constants import *
from software.thunderscope.proto_unix_io import ProtoUnixIO

from software.thunderscope.gl.layers.gl_layer import GLLayer
from software.thunderscope.gl.helpers.extended_gl_view_widget import MouseInSceneEvent


class GLDrawPolygonObstacleLayer(GLLayer):
    def __init__(self, name, fullsystem_io: ProtoUnixIO) -> None:
        super().__init__(name)

        self.fullsystem_io: ProtoUnixIO = fullsystem_io

        self.polygon = GLPolygon(parent_item=self, line_width=2)
        self.points = []
        self.obstacles = []

    def add_one_point(self, point: tuple[float, float]):
        if len(self.points) == 0:
            self.points.append(point)
            self.polygon.set_points(self.points)
            return 

        if len(self.points) == 1:
            first_point = self.points[0] 
            self.points.append(point)
            self.points.append(first_point)
            self.polygon.set_points(self.points)
            return 

        first_point = self.points[0] 
        end_point = self.points.pop()

        self.points.append(point)
        self.points.append(first_point)
        self.polygon.set_points(self.points)

        # sending stuff to proto unix io
        # polygon  in c++ does not need the endpoint!
        points = [Point(x_meters=point[0], y_meters=point[1]) for point in self.points[:-1]]
        polygon = Polygon(points=points)
        obstacle = Obstacle(polygon=polygon)

        self.fullsystem_io.send_proto(ObstacleListTwo, ObstacleListTwo(obstacles=[obstacle]))

    def mouse_in_scene_pressed(self, event: MouseInSceneEvent) -> None:
        point = event.point_in_scene
        print("I've added point: {}".format(point))
        self.add_one_point((point.x(), point.y()))

        return super().mouse_in_scene_pressed(event)

    def refresh_graphics(self) -> None:
        # print("I am being updated")
        return super().refresh_graphics()
