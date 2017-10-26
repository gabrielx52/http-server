# -*- coding: utf-8 -*-
"""Server package for echo server."""
import sys
import socket
import email.utils


def server():  # pragma: no cover
    """Start a server and echo all responses."""
    port = 5071
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
            clean_request = incoming_message.replace(b'@#FULL_STOP#@', b'')
            parsed = parse_request(clean_request)
            conn.sendall(parsed)
            conn.close()
    except KeyboardInterrupt:
        if conn:
            conn.close()
        server.close()
        sys.exit()
        print("\nGoodbye")


def response_ok(uri):
    """Set up socket and connection."""
    date_time = email.utils.formatdate(usegmt=True)
    return ("HTTP/1.1 200 OK\r\n" + "Date: " + date_time +
            "\r\nResponse URI: {}\r\n\r\n").format(uri).encode('utf8')


def response_error(code, phrase):
    """Response for 500 Internal Server Error."""
    date_time = email.utils.formatdate(usegmt=True)
    return ("HTTP/1.1 {} {}\r\nDate: " +
            date_time + "\r\n\r\n").format(code, phrase).encode('utf8')


def parse_request(request):
    """Parse the client request to confirm validity."""
    if request.endswith(b'\r\n\r\n'):
        try:
            split_header = request.split(b"\r\n")
            head, host = split_header[0], split_header[1]
            method, uri, protocol = head.split(b' ')
            host_url = host[6:]
            if method != (b"GET"):
                return response_error("405", "Method not allowed.")
            if not host_url.startswith(b"www."):
                return response_error("400", "Bad request.")
            if not host.startswith(b"Host:"):
                return response_error("400", "Bad request.")
            if protocol != (b"HTTP/1.1"):
                return response_error("505", "HTTP version not supported.")
            else:
                return response_ok(uri.decode('utf8'))
        except TypeError:
            return response_error("400", "Bad request.")
    else:
        return response_error("400", "Bad request.")


if __name__ == "__main__":  # pragma: no cover
    server()
