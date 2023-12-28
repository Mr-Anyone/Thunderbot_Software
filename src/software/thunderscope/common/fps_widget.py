import time
from PyQt6.QtWidgets import *
from pyqtgraph.graphicsItems.PlotDataItem import dataType

class FrameTimeCounter():
    def __init__(self) -> None:
        self.datapoints = []  # stores the timeframe of every data cycle
        self.previous_timestamp = time.time()

    def add_one_datapoint(self):
        current_time = time.time()
        self.datapoints.append(current_time - self.previous_timestamp)
        self.previous_timestamp = current_time

    def get_last_frametime(self):
        # return unit in s
        if len(self.datapoints)  <2:
            return -1

        return self.datapoints[-1]

    def get_average_frametime(self):
        if len(self.datapoints) == 0:
            return -1

        return sum(self.datapoints) / len(self.datapoints)


class FrameTimeWidget(QWidget):
    def __init__(self, counter:FrameTimeCounter):
        QWidget.__init__(self)
        self.counter = counter

        self.fps_label = QLabel("some string to be show") 
        self.fps_label.setText("some fps: ")
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.fps_label)

        self.setLayout(self.vertical_layout)

    def refresh(self):
        frametime = self.counter.get_last_frametime() * 1000
        average_frametime = self.counter.get_average_frametime() * 1000

        # fps
        average_fps =  1/(average_frametime/1000)
        fps =  1/(frametime/1000)

        self.fps_label.setText(f"frametime: {frametime:3f} fps: {fps:3f}\naverage frametime: {average_frametime:3f} average fps: {average_fps:3f}")

