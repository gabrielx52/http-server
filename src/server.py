"""Server package for echo server."""

import socket
import sys


def server():
    """Start a server and echo all responses."""
    port = 5033
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', port))
    server.listen(1)
    try:
        while True:
            conn, addr = server.accept()
            buffer_length = 8
            message_complete = False
            incoming_message = ''
            while not message_complete:
                part = conn.recv(buffer_length)
                incoming_message += part.decode('utf8')
                if len(part) < buffer_length:
                    conn.sendall(incoming_message.encode('utf8'))
                    conn.close()
                    break
    except KeyboardInterrupt:
        server.close()
        print("\nGoodbye")
        sys.exit()
