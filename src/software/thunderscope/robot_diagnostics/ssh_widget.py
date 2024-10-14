import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.Qt.QtWidgets import *
from software.py_constants import *
import time as time

class SSHWidget(QWidget):
    def __init__(self, robot_id: int) -> None:
        super().__init__()
        self.robot_id = robot_id 

        self.pinable_widget = QLabel("Ping: No Good")
        self.sshable_widget = QLabel("SSH Status: No Good")
        self.systemd_widget = QLabel("Systemd Status: Active")
        self.robot_channel = QLabel("Robot Channel: Active")
        self.flash_button = QPushButton("Flash Robot")

        self.layout = QHBoxLayout()

        # adding the widget into stuff
        self.layout.addWidget(self.pinable_widget)
        self.layout.addWidget(self.sshable_widget)
        self.layout.addWidget(self.systemd_widget)
        self.layout.addWidget(self.robot_channel)
        self.layout.addWidget(self.flash_button)

        self.setLayout(self.layout)
