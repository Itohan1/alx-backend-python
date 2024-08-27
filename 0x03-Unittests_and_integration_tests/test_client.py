#!/usr/bin/env python3
"""
    Familiarize yourself with the
    client.GithubOrgClient class
"""
from client import GithubOrgClient
from utils import get_json, memoize
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from typing import Dict, Optional, List
from fixtures import TEST_PAYLOAD


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
        with patch.object(
                GithubOrgClient, '_public_repos_url',
                new_callable=PropertyMock
                ) as mock_last:
            obj = GithubOrgClient("google")
            mock_last.return_value = "https://api.github.com/orgs/google/repos"
            result = obj.public_repos()
            expected = ["truth", "ruby-openid-apps-discovery", "autoparse"]
            self.assertEqual(result, expected)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
            self, repo: Dict[str, Dict],
            license_key: str, result: bool) -> None:
        """Check for license"""

        check = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(check, result)


@parameterized_class(
        ("org_payload", "repos_payload",
            "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test: fixtures"""

    @classmethod
    def setUpClass(cls):
        """Setting up a class method"""

        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            """Checking if urls are properly set"""

            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload
            return {}
        cls.mock_get.return_value.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tearing down a class method"""
        cls.get_patcher.stop()

    def tear_some(self):
        """Testing class methods"""
        self.mock_get.return_value.status_code = 200
        self.assertEqual(self.mock_get.return_value.status_code, 200)


if __name__ == "__main__":
    unittest.main()
