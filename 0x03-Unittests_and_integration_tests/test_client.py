#!/usr/bin/env python3
"""
    Familiarize yourself with the
    client.GithubOrgClient class
"""
from client import GithubOrgClient
from utils import get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators"""

    @parameterized.expand([
        ("google"),
        ("abc")
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

    def test_public_repos_url(self):
        """Mocking a property"""

        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock
                ) as mock_last:
            mock_last.return_value = {
                    'repos_url':
                    'https://api.github.com/orgs/google/repos'
            }
            obj = GithubOrgClient("google")
            result = obj._public_repos_url
            expected = 'https://api.github.com/orgs/google/repos'
            self.assertEqual(result, expected)

    @patch('client.get_json')
    def test_public_repos(self, mock_first: Mock) -> None:
        """More patching"""

        mock_first.return_value = [
                {"name": "truth"},
                {"name": "ruby-openid-apps-discovery"},
                {"name": "autoparse"}
        ]
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_last:
            obj = GithubOrgClient("google")
            mock_last.return_value = "https://api.github.com/orgs/google/repos"
            result = obj.public_repos()
            expected = ["truth", "ruby-openid-apps-discovery", "autoparse"]
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
