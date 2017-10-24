"""Client package for echo server."""

import socket


def client(message):
    """Connect with server and send message."""
    port = 5033
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
    print(incoming_message)
    client.close()





 if __name__ == "__main__": 