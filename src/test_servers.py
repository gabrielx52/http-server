"""Test our Client-Server connection."""


# import pytest


def test_client():
    """Function tests that the server performs as planned."""
    from client import client
    reply = client('This is a test!')
    print(reply)
    assert reply == 'This is a test!'


def test_client_message_is_shorter_than_buffer():
    """Function tests that the server performs as planned."""
    from client import client
    reply = client('a test')
    print(reply)
    assert reply == 'a test'


def test_client_message_is_much_longer_than_buffer():
    """Function tests that the server performs as planned."""
    from client import client
    reply = client('This is a test of the emergency broadcast system. This is only a test.')
    print(reply)
    assert reply == 'This is a test of the emergency broadcast system. This is only a test.'
"""
The following conditions should be tested:

messages shorter than one buffer in length
messages longer than several buffers in length
messages that are an exact multiple of one buffer in length
messages containing non-ascii characters
"""
