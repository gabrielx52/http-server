# -*- coding: utf-8 -*-
"""Client package for echo server."""
from __future__ import unicode_literals
import socket
import sys
import codecs


def client(message):
    """Connect with server and send message."""
    port = 5081
    message += '@#FULL_STOP#@'
    client = socket.socket(*socket.getaddrinfo('127.0.0.1', port)[1][:3])
    client.connect(('127.0.0.1', port))
    request = codecs.escape_decode(message)[0]
    client.sendall(request)
    buffer_length = 8
    reply_complete = False
    incoming_message = b''
    while not reply_complete:
        part = client.recv(buffer_length)
        incoming_message += part
        if incoming_message.endswith(b'@FULL_STOP@'):
            reply_complete = True
    client.shutdown(socket.SHUT_WR)
    client.close()
    clean_response = incoming_message.replace(b'@FULL_STOP@', b'')
    return clean_response.decode('utf8')


if __name__ == "__main__":
    print(client(sys.argv[1]))
