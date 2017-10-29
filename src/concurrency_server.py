# -*- coding: utf-8 -*-
"""Async server using gevent."""
from __future__ import unicode_literals
import server
import sys


def async_server(socket, address):  # pragma: no cover
    """Async server function."""
    try:
        while True:
            buffer_length = 8
            message_complete = False
            incoming_message = b''
            while not message_complete:
                part = socket.recv(buffer_length)
                incoming_message += part
                if b'@#FULL_STOP#@' in incoming_message:
                    message_complete = True
            clean_request = incoming_message.replace(b'@#FULL_STOP#@', b'')
            parsed = server.parse_request(clean_request)
            socket.sendall(parsed)
            socket.close()
    except KeyboardInterrupt:
        if socket:
            socket.close()
        sys.exit()
        print("\nGoodbye")


if __name__ == '__main__':  # pragma: no cover
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    s_server = StreamServer(('127.0.0.1', 5081), async_server)
    print('Starting echo server on port 5061')
    s_server.serve_forever()
