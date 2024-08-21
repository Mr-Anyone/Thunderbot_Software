# import os 
# os.add_dll_directory("C:/Users/Vince/AppData/Local/Programs/Python/Python311/Lib/site-packages/PyQt6/Qt6/bin")

# from software.thunderscope.thunderscope import Thunderscope
from software.py_constants import *
import software.python_bindings as tbots_cpp
# from software.thunderscope.robot_communication import RobotCommunication
# from software.thunderscope.constants import EstopMode, ProtoUnixIOTypes
# from software.thunderscope.estop_helpers import get_estop_config
# from software.thunderscope.proto_unix_io import ProtoUnixIO
# import software.thunderscope.thunderscope_config as config



if __name__ == "__main__":
    print(SSL_REFEREE_ADDRESS)
    print(tbots_cpp)
    # # placholder
    # tscope_config = config.configure_ai_or_diagnostics(
    #     False,
    #     False,
    #     True,
    #     5
    # )
    # tscope = Thunderscope(config=tscope_config, layout_path=None)

    # # this will be the current fullsystem proto (blue or yellow)
    # # if fullsystem is loaded
    # # else, it will be the diagnostics proto
    # current_proto_unix_io = tscope.proto_unix_io_map[ProtoUnixIOTypes.CURRENT]

    # estop_mode, estop_path = get_estop_config(
    #         # disable communication and keyboard estop
    #     True, False
    # )

    # with RobotCommunication(
    #     current_proto_unix_io=current_proto_unix_io,
    #     multicast_channel=getRobotMulticastChannel(0),
    #     interface="enp3s0",
    #     estop_mode=estop_mode,
    #     estop_path=estop_path,
    #     enable_radio=False,
    # ) as robot_communication:

    #     if estop_mode == EstopMode.KEYBOARD_ESTOP:
    #         tscope.keyboard_estop_shortcut.activated.connect(
    #             robot_communication.toggle_keyboard_estop
    #         )

    #     for tab in tscope_config.tabs:
    #         if hasattr(tab, "widgets"):
    #             robot_view_widget = tab.find_widget("Robot View")

    #             if robot_view_widget:
    #                 robot_view_widget.control_mode_signal.connect(
    #                     lambda mode, robot_id: robot_communication.toggle_robot_connection(
    #                         mode, robot_id
    #                     )
    #                 )

    #     tscope.show()
