import time
import os
os.add_dll_directory("C:/Program Files (x86)/g3log/bin")
import software.python_bindings as tbots_cpp
from proto.import_all_protos import *
from threading import Lock


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
def test_basic():
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


class AtmoicCounter: 
    def __init__(self, count):
        self.count = count
        self.mutex = Lock()

    def get_count(self):
        with self.mutex:
            return self.count

    def increment_count(self):
        with self.mutex:
            self.count += 1

def test_multicast():
    port = 10002
    address = "ff02::c3d0:42d2:bb00"
    is_multicast = True 

    counter = AtmoicCounter(0)
    primitive_set_listener = tbots_cpp.PrimitiveSetProtoListener(
        address, port, lambda x: counter.increment_count(), is_multicast
    )

    primitive_set_listener2 = tbots_cpp.PrimitiveSetProtoListener(
        address, port, lambda x: counter.increment_count(), is_multicast
    )

    # address, port, is_multicast
    primitive_set_sender = tbots_cpp.PrimitiveSetProtoUdpSender(
        address, port, is_multicast
    )

    # some data and sending proto
    some_primitive_set = PrimitiveSet(
        stay_away_from_ball=True,
    )

    send_count = 1000
    for i in range(send_count):    
        primitive_set_sender.send_proto(some_primitive_set) 
    
    # wait for 5 seconds to see if it can pass the test!
    start_time = time.time() 
    while time.time() - start_time < 5 and counter.get_count() != send_count * 2:
        time.sleep(0.1)

    assert counter.get_count() == send_count * 2
    print("Yay I've passed the")

if __name__ == "__main__":
    """Please read the header of this file for more context on what it is testing!"""
    test_basic()
    test_multicast()