#!/usr/bin/env python3
"""
    Create a TestAccessNestedMap
    class that inherits from unittest.TestCase
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """write the first unit test for utils.access_nested_map"""

    @parameterized.expand([
            ({"a": 1}, ("a",)),
            ({"a": {"b": 2}}, ("a",)),
            ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence) -> Any:
        """"""

        result = access_nested_map(nested_map, path)
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
