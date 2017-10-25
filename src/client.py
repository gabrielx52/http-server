# -*- coding: utf-8 -*-
"""Client package for echo server."""
import socket
import sys


def client(message):
    """Connect with server and send message."""
    port = 5059
    message += '@#FULL_STOP#@'
    client = socket.socket(*socket.getaddrinfo('127.0.0.1', port)[1][:3])
    client.connect(('127.0.0.1', port))
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    reply_complete = False
    incoming_message = b''
    while not reply_complete:
        part = client.recv(buffer_length)
        incoming_message += part
        if incoming_message.endswith(b'\r\n\r\n'):
            reply_complete = True
    client.shutdown(socket.SHUT_WR)
    client.close()
    return incoming_message.decode('utf8')

if __name__ == "__main__":
    print(client(sys.argv[1]))
