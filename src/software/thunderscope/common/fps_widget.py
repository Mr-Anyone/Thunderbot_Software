import time
from PyQt6.QtWidgets import *
import os

class FrameTimeCounter():
    def __init__(self, name=None, filename=None) -> None:
        self.datapoints = []  # stores the timeframe of every data cycle
        self.previous_timestamp = time.time()

        directories = os.listdir("/tmp/tbots/thunderscope-profile")
        directories = sorted(directories, reverse=True)
        save_dir = "/tmp/tbots/thunderscope-profile/" + directories[0]

        if filename is None:
            self.filename = f"{save_dir}/{time.time()}.csv"
        else:
            self.filename = f"{save_dir}/{filename}-{time.time()}.csv"

        self.log_file = open(self.filename, "w")
        self.log_file.write("current time, last frametime\n")

    def add_one_datapoint(self):
        current_time = time.time()
        self.datapoints.append(current_time - self.previous_timestamp)
        self.previous_timestamp = current_time

        self.log_file.write(f"{time.time()}, {self.get_last_frametime()}\n")

    def get_last_frametime(self):
        # return unit in s
        if len(self.datapoints)  <2:
            return -1

        return self.datapoints[-1]

    def get_average_frametime(self):
        if len(self.datapoints) == 0:
            return -1

        self.report_fps_and_frametime()
        return sum(self.datapoints) / len(self.datapoints)

    def get_average_last_30(self):
        if (len(self.datapoints) == 0):
            return -1

        return sum(self.datapoints[-30:]) / 30

    def get_average_all(self):
        if (len(self.datapoints) == 0):
            return -1

        return sum(self.datapoints) / len(self.datapoints)


class FrameTimeWidget(QWidget):
    def __init__(self, buffer_counter:FrameTimeCounter, refresh_counter: FrameTimeCounter):
        super().__init__()
        self.buffer_counter = buffer_counter
        self.refresh_counter = refresh_counter

        self.fps_label = QLabel("some string to be show") 
        self.fps_label.setText("some fps: ")
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.fps_label)

        self.setLayout(self.vertical_layout)

    def refresh(self):
        frametime = self.buffer_counter.get_last_frametime() * 1000
        average_last_30  = self.buffer_counter.get_average_last_30() * 1000
        frametime_average_all = self.buffer_counter.get_average_all() * 1000
        fps =  1/(frametime/1000)
        average_last_30_fps = 1/(average_last_30/1000)
        fps_all = 1/(frametime_average_all/1000)

        refresh_func_frametime = self.refresh_counter.get_last_frametime() * 1000
        refresh_func_average_last_30  = self.refresh_counter.get_average_last_30() * 1000
        refresh_func_frametime_average_all = self.refresh_counter.get_average_all() * 1000
        refresh_func_fps =  1/(refresh_func_frametime/1000)
        refresh_func_average_last_30_fps = 1/(refresh_func_average_last_30/1000)
        refresh_func_fps_all = 1/(refresh_func_frametime_average_all/1000)

        display_text = f"""
        Bufferswap time:
        frametime: {frametime} 
        fps: {fps:3f}\n
        last 30: {average_last_30} 
        last 30_fps: {average_last_30_fps}\n
        frametime all: {frametime_average_all}
        fps_all: {fps_all}\n  
        
        Refresh Function:
        frametime: {refresh_func_frametime} 
        fps: {refresh_func_fps:3f}\n
        last 30: {refresh_func_average_last_30} 
        last 30_fps: {refresh_func_average_last_30_fps}\n
        frametime all: {refresh_func_frametime_average_all}
        fps_all: {refresh_func_fps_all}\n  

        """

        self.fps_label.setText(display_text)
