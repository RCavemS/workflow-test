"""Tests for the hello script."""

import unittest
from hello import get_greeting


class TestHello(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(get_greeting(), "Hello, world!")

    def test_custom_greeting(self):
        self.assertEqual(get_greeting("Alice"), "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
