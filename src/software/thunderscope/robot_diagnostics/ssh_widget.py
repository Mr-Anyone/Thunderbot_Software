import socket
import subprocess
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.Qt.QtWidgets import *
from software.py_constants import *
import time as time

class SSHWidget(QWidget):
    def __init__(self, robot_id: int) -> None:
        super().__init__()

        self.robot_id = robot_id 
        # TODO: fix this later!
        name = "bruhbot"
        
        self.hostnames = [f"{name}{sufix}.local" for sufix in ["jetson", ""]]
        self.password = "nice try" 


        self.pinable_widget = QLabel("Ping: No Good")
        self.sshable_widget = QLabel("SSH Status: No Good")
        self.systemd_widget = QLabel("Systemd Status: Active")
        self.robot_channel = QLabel("Robot Channel: Active")
        self.flash_button = QPushButton("Flash Robot")
        self.enter_password_widget = QTextEdit("enter ssh password: ")

        self.systemd_output = QLabel("systemd outout:")

        self.enter_password_widget.textChanged.connect(self.set_password)
        self.flash_button.clicked.connect(self.check_systemd_status)

        self.fullLayout = QVBoxLayout()
        self.layout = QHBoxLayout()

        # adding the widget into stuff
        self.layout.addWidget(self.pinable_widget)
        self.layout.addWidget(self.sshable_widget)
        self.layout.addWidget(self.systemd_widget)
        self.layout.addWidget(self.robot_channel)
        self.layout.addWidget(self.flash_button)

        self.fullLayout.addWidget(self.enter_password_widget)
        self.fullLayout.addWidget(self.systemd_output)
        self.fullLayout.addLayout(self.layout)
        self.setLayout(self.fullLayout)

    def set_password(self):
        # we can now set password 
        self.password = self.enter_password_widget.toPlainText()

    def send_command_ssh(self, command):
        for hostname in self.hostnames:
            try:
                # Construct the SSH command
                ssh_command = ['sshpass', '-p', self.password, 'ssh', f'robot@{hostname}', command]
                print(f"sending ssh command{ssh_command}")

                # Run the command
                result = subprocess.run(ssh_command, capture_output=True, text=True, check=True)
                print(f"the result is : {result.stdout}")

                # Print the output and errors
                if result.stdout:
                    return result.stdout

            except Exception as e: 
                print("I got exception e: {}".format(e))

        raise Exception("cannot send command through ssh")

    def is_systemd_active_from_text(self, text):
        return "active (running)" in text

    def check_systemd_status(self):
        try:
            systemd_output = self.send_command_ssh(f"echo {self.password} | sudo -S systemctl status thunderloop")

            self.systemd_output.setText(systemd_output)
            if self.is_systemd_active_from_text(systemd_output):
                self.systemd_widget.setText("systemd: active") 

        except Exception as e:
            print("I got an exception e: {}".format(e))

    def is_pinable(self):
        # this is the ssh port and this should work?
        port = 22
        timeout = 5
        try:
            socket.create_connection((host, port), timeout)
            return True
        except (socket.timeout, OSError):
            return False

