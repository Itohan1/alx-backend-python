#!/usr/bin/env python3
"""
    Familiarize yourself with the
    client.GithubOrgClient class
"""
from client import GithubOrgClient
from utils import get_json
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators"""

    @parameterized.expand([
        ("google"),
        ("org")
    ])
    @patch('client.get_json')
    def test_org(self, org_value: str, mock_get: Mock) -> None:
        """
            This method should test that
            GithubOrgClient.org returns the
            correct value
        """

        client = GithubOrgClient(org_value)
        mock_get.return_value = {"name": org_value}

        result = client.org

        mock_get.assert_called_once_with(
                f"https://api.github.com/orgs/{org_value}")
        self.assertEqual(result, {"name": org_value})


if __name__ == "__main__":
    unittest.main()
