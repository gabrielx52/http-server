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
                if b'@#FULL_STOP#@' in incoming_message:
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


def response_error(code, phrase):
    """Response for 500 Internal Server Error."""
    date_time = email.utils.formatdate(usegmt=True)
    return ("HTTP/1.1 {} {}\r\nDate: " +
            date_time + "\r\n\r\n").format(code, phrase)


def parse_request(request):
    """Parse the client request to confirm validity."""
    if request.endswith('\r\n\r\n'):
        head, host, *_ = request.split("\r\n")
        method, uri, protocol = head.split(' ')
        host_url = host[6:]
        if method != ("GET"):
            raise TypeError("Your method request must be that of GET.")
        if not host_url.startswith("www.") and not host.startswith("Host:"):
            raise ValueError("Your requested url is not properly formatted or\
                            could not be found.")
        if protocol != ("HTTP/1.1"):
            raise ValueError("Your request is not of the proper protocol.")
        else:
            return uri
    else:
        raise ValueError("Your requested url is not properly formatted")


if __name__ == "__main__":
    server()
