"""Client package for echo server."""

import socket
import sys


def client(message):
    """Connect with server and send message."""
    port = 5042
    if len(message) % 8 == 0:
        message += ' '
    client = socket.socket(*socket.getaddrinfo('127.0.0.1', port)[1][:3])
    client.connect(('127.0.0.1', port))
    client.sendall(message.encode('utf8'))
    buffer_length = 8
    reply_complete = False
    incoming_message = ''
    while not reply_complete:
        part = client.recv(buffer_length)
        incoming_message += part.decode('utf8')
        if len(part) < buffer_length:
            break
    client.close()
    print(incoming_message.strip())
    return(incoming_message.strip())


if __name__ == "__main__":
    client(sys.argv[1])
