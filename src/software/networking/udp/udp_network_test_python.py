import time

import os
os.add_dll_directory("C:/Program Files (x86)/g3log/bin")
import software.python_bindings as tbots_cpp

from proto.import_all_protos import *


def wait_for(sec, some_state):
    start_time = time.time()
    while time.time() - start_time < sec and not some_state.get_state():
        time.sleep(0.1)


class TestResultPlaceholder:
    def __init__(self, start_state):
        self.state = start_state

    def set_state(self, state):
        print("A state has been set: {}".format(state))
        self.state = state

    def get_state(self):
        return self.state


# def test_network_python_bindings():
def main():
    address = "127.0.0.1"
    port = 10123
    is_multicast = False

    some_state = TestResultPlaceholder(False)

    def another_wrapper(state_class):
        def some_callback(proto_message):
            print(proto_message)
            print(type(proto_message))
            print("I've been executed!")

            some_state.set_state(True)
        return some_callback

    primitive_set_listener = tbots_cpp.PrimitiveSetProtoListener(
        address, port, another_wrapper(some_state), is_multicast
    )

    # address, port, is_multicast
    primitive_set_sender = tbots_cpp.PrimitiveSetProtoUdpSender(
        address, port, is_multicast
    )

    some_primitive_set = PrimitiveSet(
        stay_away_from_ball=True,
    )
    
    primitive_set_sender.send_proto(some_primitive_set)

    wait_for(10, some_state)
    assert some_state.get_state()

    print("I have got the message!")


if __name__ == "__main__":
    """Please read the header of this file for more context on what it is testing!"""
    main()