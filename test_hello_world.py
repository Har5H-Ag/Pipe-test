import pytest
from hello_world import greet

def test_greet_default():
    assert greet() == "Hello, World!"

def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!" 