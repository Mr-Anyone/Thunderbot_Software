import time
import os

os.add_dll_directory("C:/Program Files (x86)/g3log/bin")
import software.python_bindings as tbots_cpp
from proto.import_all_protos import *

address = "ff02::c3d0:42d2:bb00"
port = 12345
multicast = True 

def callback(message): 
    print(f"I've got the message: {message.log_msg}")

if __name__ == "__main__":
    receive_robot_log = tbots_cpp.RobotLogProtoListener(
        address,
        port,
        callback,
        True,
    )

    while True: 
        some_input = input("do you want to break?") 
        if some_input == "yes":
            break 

        time.sleep(5)