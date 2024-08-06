import socket
import os

# Set the path for the Unix socket
socket_path = '/tmp/testing.sock'

# remove the socket file if it already exists
try:
    os.unlink(socket_path)
except OSError:
    if os.path.exists(socket_path):
        raise

# Create the Unix socket server
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

# Bind the socket to the path
server.bind(socket_path)

# receive data from the client
data = server.recv(1024)
print('Received data:', data.decode())

os.unlink(socket_path)
