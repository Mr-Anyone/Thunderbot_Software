import base64
import os
import queue
import socketserver
from threading import Thread
from software.logger.logger import createLogger
from software import py_constants
from proto.import_all_protos import *

logger = createLogger(__name__)

import proto
from google.protobuf.any_pb2 import Any


class ThreadedUnixListener:
    def __init__(
            self, unix_path, proto_class=None, is_base64_encoded=False, max_buffer_size=100
    ):

        """Receive protobuf over unix sockets and buffers them

        :param unix_path: The unix path to receive the new protobuf to plot
        :param proto_class: The protobuf to unpack from (None if its encoded in the payload)
        :param is_base64_encoded: If the data is is_base64_encoded, we need to decode it first
                               before grabbing the protobuf. This is required for
                               LOG(VISUALIZE) calls where the data needs to be is_base64_encoded
                               to avoid \n characters.

        :param max_buffer_size: The size of the buffer

        """

        # cleanup the old path if it exists
        try:
            os.remove(unix_path)
        except:
            pass

        self.proto_buffer = queue.Queue(max_buffer_size)

        # TODO: Python3.12 adds ForkingUnixDatagramServer which launch another process
        #  (true parallelism for CPU bound apps)
        self.server = socketserver.ThreadingUnixDatagramServer(
            unix_path,
            ProtoRequestHandler,
        )
        self.server.daemon_threads = True
        self.server.max_packet_size = py_constants.UNIX_BUFFER_SIZE

        # Add new attributes to the server object so that we can access them
        # in the handler
        self.server.is_base64_encoded = is_base64_encoded
        self.server.proto_class = proto_class
        self.server.buffer = self.proto_buffer

        # Start the server in a separate thread, so it is not blocking
        # the main thread.
        # We want to set daemon to true so that the program can exit
        # even if there are still unix listener threads running
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def force_stop(self):
        """Stop handling requests
        """
        self.server.server_close()


class ProtoRequestHandler(socketserver.BaseRequestHandler):
    """
    Handler class created for each request from the unix sender.

    self.server refers to the ThreadingUnixDatagramServer which holds
    references to the ThreadedUnixListener fields.
    """

    def handle(self):
        """Handle proto

        """
        print(f"Received {self.server.proto_class.DESCRIPTOR.full_name}")
        if not self.server.is_base64_encoded:
            self.handle_proto()
        else:
            self.handle_log_visualize()

    def handle_proto(self):
        """If a specific protobuf class is passed in, this handler is called.

        It deserializes the incoming msg into the class and triggers the
        handle callback.

        """
        if self.server.proto_class:
            self.__buffer_protobuf(self.server.proto_class.FromString(self.request[0]))
        else:
            raise Exception("proto_class is None but handle_proto called")

    def handle_log_visualize(self):
        """We send protobufs from our C++ code to python for visualization.
        The C++ logger encodes a serialized anyproto with base64 and sends it over.
        We need to apply the reverse sequence of operations to unpack the data.

        """
        payload = self.request[0]

        # Unpack metadata
        path, protobuf_type, payload = payload.split(
            bytes("!!!", encoding="utf-8")
        )

        # Convert string to type. eval is an order of magnitude
        # faster than iterating over the protobuf library to find
        # the type from the string.
        try:
            # The format of the protobuf type is:
            # package.proto_class (e.g. TbotsProto.Primitive)
            proto_class = eval(str(protobuf_type.split(b".")[-1], encoding="utf-8"))
        except Exception as e:
            logger.error("Failed to eval protobuf type: {}".format(e))
            return

        result = base64.b64decode(payload)
        msg = proto_class()

        any_msg = Any.FromString(result)
        any_msg.Unpack(msg)
        self.__buffer_protobuf(msg)

    def __buffer_protobuf(self, proto_msg):
        """Buffer the protobuf, and raise a warning if we overrun the buffer

        :param proto_msg: The protobuf to buffer
        :raises: Warning

        """
        try:
            self.server.buffer.put_nowait(proto_msg)
        except queue.Full as queue_full:
            logger.warning(f"buffer overrun for {self.server.proto_class.DESCRIPTOR.full_name}")
