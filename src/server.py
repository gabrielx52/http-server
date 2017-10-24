"""Server package for echo server."""
import socket
import email.utils


def server():
    """Start a server and echo all responses."""
    port = 5045
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
                    response = response_ok()
                    print(incoming_message)
                    conn.sendall(response.encode('utf8'))
                    conn.close()
                    break
    except KeyboardInterrupt:
        server.close()
        print("\nGoodbye")


def response_ok():
    """Set up socket and connection."""
    date_time = email.utils.formatdate(usegmt=True)
    return "HTTP/1.1 200 OK<CRLF>\r\n" + "Date: " + date_time\
           + "<CRLF>\r\n" + "<CRLF>\r\n"


def response_error():
    """Response for 500 Internal Server Error."""
    date_time = email.utils.formatdate(usegmt=True)
    return "HTTP/1.1 500 Internal Server Error<CRLF>\r\n" + "Date: "\
           + date_time + "<CRLF>\r\n" + "<CRLF>\r\n"


if __name__ == "__main__":
    server()
