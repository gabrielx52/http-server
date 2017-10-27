# -*- coding: utf-8 -*-
"""Server package for echo server."""
import sys
import socket
import email.utils
import pathlib
import mimetypes


def server():  # pragma: no cover
    """Start a server and echo all responses."""
    port = 5087
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


def response_ok(content, cont_type):
    """Set up socket and connection."""
    date_time = email.utils.formatdate(usegmt=True)
    return ("HTTP/1.1 200 OK\r\n" + "Date: " + date_time +
            "\r\nContent-Length: {}\r\nContent-Type: \
{}\r\n\r\n{}@FULL_STOP@").format(str(len(content.encode('utf8'))),
                                 cont_type, content).encode('utf8')


def response_error(code, phrase):
    """Response for 500 Internal Server Error."""
    date_time = email.utils.formatdate(usegmt=True)
    return ("HTTP/1.1 {} {}\r\nDate: " +
            date_time + "\r\n\r\n@FULL_STOP@").format(code, phrase).encode('utf8')


def resolve_uri(uri):
    """Respose body composer with URI details and type."""
    root_path = pathlib.Path('./webroot')
    resource_path = root_path / uri.lstrip('/')
    if resource_path.is_dir():
        li_temp = '\t<li>{}</li>'
        listing = []
        for item_path in resource_path.iterdir():
            listing.append(li_temp.format(str(item_path)))
        joined_listing = "\r\n".join(listing)
        content = "<ul>\r\n{}\r\n</ul>".format(joined_listing)
        cont_type = "directory"
        return content, cont_type
    elif resource_path.is_file():
        content = ''
        with resource_path.open() as file:
            content = file.read()
        cont_type = mimetypes.guess_type(str(resource_path))[0]
        return content, cont_type


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
                try:
                    cont, cont_type = resolve_uri(uri.decode('utf8'))
                    return response_ok(cont, cont_type)
                except ValueError:
                    response_error("400", "Bad request.")
        except TypeError:
            return response_error("400", "Bad request.")
    else:
        return response_error("400", "Bad request.")


if __name__ == "__main__":  # pragma: no cover
    server()
