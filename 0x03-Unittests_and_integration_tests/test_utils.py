#!/usr/bin/env python3
"""
    Create a TestAccessNestedMap
    class that inherits from unittest.TestCase
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """write the first unit test for utils.access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence,
            expected_result: Any) -> Any:
        """
            method to test that the method
            returns what it is supposed to
        """

        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Sequence) -> Any:
        """Use the assertRaises context manager"""

        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self, test_url: str, test_payload: Dict,
            mock_get: Mock) -> None:
        """"""

        mock = Mock()
        mock.json.return_value = test_payload
        mock_get.return_value = mock
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
