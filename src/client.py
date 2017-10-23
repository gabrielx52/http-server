"""Client package for echo server."""

import socket

client = socket.socket(*socket.getaddrinfo('127.0.0.1', 5000)[1][:3])
client.connect(('127.0.0.1', 5000))
client.sendall('Hello from the client socket')
