"""Test our Client-Server connection."""
# coding=utf-8


def test_client():
    """Function tests that the server performs as planned."""
    from client import client
    reply = client('This is a test!')
    assert reply == 'This is a test!'


def test_client_message_is_shorter_than_buffer():
    """Function tests that the server performs as planned."""
    from client import client
    reply = client('a test')
    assert reply == 'a test'


def test_client_message_is_much_longer_than_buffer():
    """Function tests that the server performs as planned."""
    from client import client
    reply = client('This is a test of the emergency broadcast\
 system. This is only a test.')
    assert reply == 'This is a test of the emergency broadcast\
 system. This is only a test.'


def test_client_message_same_as_buffer_length():
    """Testing echo server with buffer sized message."""
    from client import client
    reply = client('12345678')
    assert reply == '12345678'


def test_non_ascii_characters_echo_server():
    """Test echo server with non-ascii characters."""
    from client import client
    reply = client(u'Hüsker Dü')
    assert reply == u'Hüsker Dü'
