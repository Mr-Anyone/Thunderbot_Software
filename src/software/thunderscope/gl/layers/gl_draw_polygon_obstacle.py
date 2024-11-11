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
import pudb


class GLDrawPolygonObstacleLayer(GLLayer):
    def __init__(
        self, name, blue_fs_io: ProtoUnixIO, yellow_fs_io: ProtoUnixIO
    ) -> None:
        super().__init__(name)

        self.blue_fu_io: ProtoUnixIO = blue_fs_io
        self.yellow_fs_io: ProtoUnixIO = yellow_fs_io

        self.current_polygon = GLPolygon(parent_item=self, line_width=2)
        self.points = []  # the current points buffer
        self.obstacles = []  # the message going to full system
        self.saved_polygons = []  # the glpolygon that is going to remain

        # self.q_shortcut = QtGui.QShortcut(QtGui.QKeySequence("q"))
        # self.q_shortcut.activated.connect(self.push_polygon)

        # self.r_shortcut = QtGui.QShortcut(QtGui.QKeySequence("r"))
        # self.r_shortcut.activated.connect(self.clear)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        # adding and pushing
        if event.key() == Qt.Key.Key_Q:
            self.push_polygon()

        # clearing
        if event.key() == Qt.Key.Key_A:
            pudb.set_trace()
            self.clear()

        return

    def clear(self):
        print("Clear has been called!")
        self.points.clear()
        self.obstacles.clear()

        self.saved_polygons.clear()
        self.current_polygon = GLPolygon(parent_item=self, line_width=2)

        self.send_to_fs()

    def push_polygon(self):
        print("push has been called!")
        points = [
            Point(x_meters=point[0], y_meters=point[1]) for point in self.points[:-1]
        ]
        polygon = Polygon(points=points)
        obstacle = Obstacle(polygon=polygon)
        self.obstacles.append(obstacle)
        self.points.clear()

        self.saved_polygons.append(self.current_polygon)
        self.current_polygon = GLPolygon(parent_item=self, line_width=2)
        self.send_to_fs()

    def add_one_point(self, point: tuple[float, float]):
        if len(self.points) < 2:
            self.points.append(point)
            self.current_polygon.set_points(self.points)
            return

        if len(self.points) == 2:
            start_point = self.points[0]

            self.points.append(point)
            self.points.append(start_point)
            self.current_polygon.set_points(self.points)

        start_point = self.points[0]
        self.points.pop()

        self.points.append(point)
        self.points.append(start_point)
        self.current_polygon.set_points(self.points)
        self.send_to_fs()

    def send_to_fs(self):
        # sending stuff to proto unix io
        # polygon  in c++ does not need the endpoint!

        obstacles = self.obstacles 

        points = [
            Point(x_meters=point[0], y_meters=point[1]) for point in self.points[:-1]
        ]
        if len(points) >= 3: 
            polygon = Polygon(points=points)
            obstacle = Obstacle(polygon=polygon)
            obstacles.append(obstacle)


        self.blue_fu_io.send_proto(
            ObstacleListTwo, ObstacleListTwo(obstacles=obstacles)
        )
        self.yellow_fs_io.send_proto(
            ObstacleListTwo, ObstacleListTwo(obstacles=obstacles)
        )

    def mouse_in_scene_pressed(self, event: MouseInSceneEvent) -> None:
        point = event.point_in_scene
        print("I've added point: {}".format(point))
        self.add_one_point((point.x(), point.y()))

        return super().mouse_in_scene_pressed(event)

    def refresh_graphics(self) -> None:
        # print("I am being updated")
        return super().refresh_graphics()
