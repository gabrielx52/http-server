"""Server package for echo server."""


import socket


server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM,
                       socket.IPPROTO_TCP)
server.bind(('127.0.0.1', 5000))
server.listen(1)
conn, addr = server.accept()
conn.recv(8)
