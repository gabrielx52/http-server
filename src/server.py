# -*- coding: utf-8 -*-
"""Server package for echo server."""
import sys
import socket
import email.utils


def server():
    """Start a server and echo all responses."""
    port = 5059
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
            incoming_message = b''
            while not message_complete:
                part = conn.recv(buffer_length)
                incoming_message += part
                if len(part) < buffer_length:
                    message_complete = True
            response = response_ok().encode('utf8')
            conn.sendall(response)
            print(incoming_message.decode('utf8'))
            conn.close()
    except KeyboardInterrupt:
        if conn:
            conn.close()
        server.close()
        sys.exit()
        print("\nGoodbye")


def response_ok():
    """Set up socket and connection."""
    date_time = email.utils.formatdate(usegmt=True)
    return "HTTP/1.1 200 OK\r\n" + "Date: " + date_time\
           + "\r\n\r\n"


def response_error():
    """Response for 500 Internal Server Error."""
    date_time = email.utils.formatdate(usegmt=True)
    return "HTTP/1.1 500 Internal Server Error\r\n" + "Date: "\
           + date_time + "\r\n\r\n"


if __name__ == "__main__":
    server()
