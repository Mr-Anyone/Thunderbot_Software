import threading
import time
import socket
import subprocess
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph.Qt.QtWidgets import *
from software.py_constants import *
from software.logger.logger import createLogger

import time as time

logger = createLogger(__name__)


class SSHWidget(QWidget):
    def __init__(self, robot_id: int) -> None:
        super().__init__()

        self.robot_id = robot_id
        # TODO: fix this later!
        # 7 is balle
        name = "balle"

        self.hostnames = [f"{name}{sufix}.local" for sufix in ["jetson", ""]]
        self.password = self.load_from_cache()

        self.pingable_widget = QLabel("Ping: ?")
        self.systemd_widget = QLabel("Systemd Status: ?")
        self.robot_channel = QLabel("Robot Channel: ?")
        self.flash_button = QPushButton("Flash Robot")
        self.enter_password_widget = QTextEdit(self.password)

        self.systemd_output = QLabel("systemd outout:")

        self.enter_password_widget.textChanged.connect(self.set_password)
        self.flash_button.clicked.connect(lambda x: x)


        self.fullLayout = QVBoxLayout()
        self.layout = QHBoxLayout()

        # adding the widget into stuff
        self.layout.addWidget(self.pingable_widget)
        self.layout.addWidget(self.systemd_widget)
        self.layout.addWidget(self.robot_channel)
        self.layout.addWidget(self.flash_button)

        self.fullLayout.addWidget(self.enter_password_widget)
        self.fullLayout.addWidget(self.systemd_output)
        self.fullLayout.addLayout(self.layout)
        self.setLayout(self.fullLayout)

        self.daemon_thread = threading.Thread(target=self.check)
        self.daemon_thread.start()

    def save_password_to_disk(self, password): 
        logger.info("I am saving password to disk!")
        with open("/opt/tbotspython/ssh_password.txt", "w") as f:
            f.write(password)

    def load_from_cache(self):
        try:
            logger.info("I am loading password from cache")

            with open("/opt/tbotspython/ssh_password.txt", "r") as f:
                return f.read()

        except Exception as e:
            logger.exception("I got exception {}".format(e))
            return "enter password here: "

         

    def set_password(self):
        # we can now set password
        self.password = self.enter_password_widget.toPlainText()
        self.save_password_to_disk(self.password)

    def check(self):
        """
        this is going to check for stuff I guess
        """

        while True:
            # for debugging purposes
            if self.robot_id  != 7:
                break

            # I can ping
            logger.info("I started one check loop?")
            if self.is_pingable():
                print("I can ping")
                self.pingable_widget.setText("Ping: Good")
            else:
                print("I cannot ping!")
                self.pingable_widget.setText("Ping: No Good")
                # there is no way you can ping but not ssh
                return

            # what is the systmemd widget?
            if self.check_systemd_status():
                self.systemd_widget.setText("Systmed Status: Active")
            else:
                self.systemd_widget.setText("Systmed Status: Inactive")

            # TODO: the following what is the robot channel id?
            channel_id = self.get_channel_id()
            self.robot_channel.setText(f"Chanel id: {str(channel_id)}")

            time.sleep(10)

    def send_command_ssh(self, command):
        for hostname in self.hostnames:
            try:
                # Construct the SSH command
                ssh_command = [
                    "sshpass",
                    "-p",
                    self.password,
                    "ssh",
                    f"robot@{hostname}",
                    command,
                ]
                print(f"sending ssh command{ssh_command}")

                # Run the command
                result = subprocess.run(
                    ssh_command, capture_output=True, text=True, check=False, timeout=10
                )
                print(f"the result is : {result.stdout}")

                # Print the output and errors
                if result.stdout:
                    return result.stdout

            except Exception as e:
                print("I got exception e: {}".format(e))

        raise Exception("cannot send command through ssh")

    # TODO:
    def stop_thunderloop(self):
        pass

    # TODO:
    def restart_thunderloop(self):
        pass

    def is_systemd_active_from_text(self, text):
        return "active (running)" in text

    # TODO: as of current, there is a bug so the user has to run ssh-keygen -R the localhost before doign this
    # I am not sure what to do about this!
    def check_systemd_status(self):
        try:
            systemd_output = self.send_command_ssh(
                f"echo {self.password} | sudo -S systemctl status thunderloop"
            )

            self.systemd_output.setText(systemd_output)
            # set when the systemd output is Active
            if self.is_systemd_active_from_text(systemd_output):
                return True

            return False
            # what to do when there is an error?
        except Exception as e:
            print("I got an exception e: {}".format(e))
            return False

    def is_pingable(self):
        # this should work if you create an ssh connection
        port = 22
        timeout = 1

        for host in self.hostnames:
            try:
                socket.create_connection((host, port), timeout)
                return True
            except (socket.timeout, OSError):
                print("timeout for: {}".format(host))
                continue

        return False

    def get_channel_id(self):
        try:
            channel_id = self.send_command_ssh("redis-cli get /channel_id").replace(
                '"', ""
            )
            return int(channel_id)
        except Exception as e:
            return -1
