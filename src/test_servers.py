"""Test our Client-Server connection."""
# coding=utf-8
from __future__ import unicode_literals

# Tests for echo server, will break with newer versions.
# Nick said it was okay to comment out.
# def test_client():
#     """Function tests that the server performs as planned."""
#     from client import client
#     reply = client('This is a test!')
#     assert reply == 'This is a test!'


# def test_client_message_is_shorter_than_buffer():
#     """Function tests that the server performs as planned."""
#     from client import client
#     reply = client('a test')
#     assert reply == 'a test'


# def test_client_message_is_much_longer_than_buffer():
#     """Function tests that the server performs as planned."""
#     from client import client
#     reply = client('This is a test of the emergency broadcast\
#  system. This is only a test.')
#     assert reply == 'This is a test of the emergency broadcast\
#  system. This is only a test.'


# def test_client_message_same_as_buffer_length():
#     """Testing echo server with buffer sized message."""
#     from client import client
#     reply = client('12345678')
#     assert reply == '12345678'


# def test_non_ascii_characters_echo_server():
#     """Test echo server with non-ascii characters."""
#     from client import client
#     reply = client(u'Hüsker Dü')
#     assert reply == u'Hüsker Dü'


def test_response_ok():
    """Test for server response_ok function."""
    from server import response_ok
    assert response_ok("body", "type").endswith(b'@FULL_STOP@')


def test_response_error():
    """Test that we get an 500 error message."""
    from server import response_error
    resp = response_error("500", 'Internal Server Error')
    assert resp.startswith(b"HTTP/1.1 500")


def test_client_message_response_ok_end():
    """Testing client response message."""
    from client import client
    reply = client('test string')
    assert reply.endswith('GMT\r\n\r\n')


def test_client_message_response_ok_start():
    """Testing client response message start."""
    from client import client
    reply = client('test string')
    assert reply.startswith('HTTP/1.1 400')


def test_parse_request_405_error():
    """Check if URI is returned from parse request function."""
    from server import parse_request
    req = b"PUT /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
    assert parse_request(req).startswith(b'HTTP/1.1 405')


def test_parse_request_400_error_bad_url():
    """Check if URI is returned from parse request function."""
    from server import parse_request
    req = b"GET /index.html HTTP/1.1\r\nHist: www.example.com\r\n\r\n"
    assert parse_request(req).startswith(b'HTTP/1.1 400')


def test_parse_request_400_error_bad_www():
    """Check if URI is returned from parse request function."""
    from server import parse_request
    req = b"GET /index.html HTTP/1.1\r\nHost: wdw.example.com\r\n\r\n"
    assert parse_request(req).startswith(b'HTTP/1.1 400')


def test_parse_request_505_error_bad_protocol():
    """Check if protocol is returned from parse request function."""
    from server import parse_request
    req = b"GET /index.html HTTP/2.1\r\nHost: www.example.com\r\n\r\n"
    assert parse_request(req).startswith(b'HTTP/1.1 505')


def test_parse_request_400_bad_request():
    """Check if URI is returned from parse request function."""
    from server import parse_request
    req = b"GET /index.html HTTP/1.1\r\nHist: www.example.com\r\n"
    assert parse_request(req).startswith(b'HTTP/1.1 400')


def test_parse_request_400_error_bad_parse_request():
    """Check if URI is returned from parse request function."""
    from server import parse_request
    req = b"GET /index.html HTTP/1.1\r\nHist: www.example.com\r\n\r\n"
    assert parse_request(req).startswith(b'HTTP/1.1 400')


def test_parse_request_return():
    """Test parse request for content and type."""
    from server import parse_request
    req = b"GET /images HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
    assert parse_request(req).startswith(b"HTTP/1.1 200 OK")


def test_resolve_uri_directory_content_type():
    """Check uri content type."""
    from server import resolve_uri
    content, cont_type = resolve_uri(u"/images")
    assert cont_type == u"directory"


def test_resolve_uri_txt_plain_content_type():
    """Check uri content type."""
    from server import resolve_uri
    content, cont_type = resolve_uri(u"/sample.txt")
    assert cont_type == u"text/plain"


def test_resolve_uri_png_content_type():
    """Check uri content type of png."""
    from server import resolve_uri
    content, cont_type = resolve_uri(u"/images/sample_1.png")
    assert cont_type == u"image/png"


def test_resolve_uri_jpg_content_type():
    """Check uri content type of jpg."""
    from server import resolve_uri
    content, cont_type = resolve_uri(u"/images/JPEG_example.jpg")
    assert cont_type == u"image/jpeg"
