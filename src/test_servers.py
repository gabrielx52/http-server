"""Test our Client-Server connection."""
# coding=utf-8

# Tests for echo server, will break with newer versions.
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
    assert response_ok().endswith('\r\n\r\n')


def test_response_error():
    """Test that we get an 500 error message."""
    from server import response_error
    assert response_error().endswith('\r\n\r\n')


def test_client_message_response_ok_end():
    """Testing client response message."""
    from client import client
    reply = client('test string')
    assert reply.endswith('GMT\r\n\r\n')


def test_client_message_response_ok_start():
    """Testing client response message start."""
    from client import client
    reply = client('test string')
    assert reply.startswith('HTTP/1.1 200 OK')


def test_status_code_response_error():
    """Testing response error returns 500 status code."""
    from server import response_error
    assert response_error().startswith('HTTP/1.1 500')

