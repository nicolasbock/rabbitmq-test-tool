"""Test get_version."""

import unittest
from unittest import mock
from unittest.mock import MagicMock

from bin import get_version


class TestGetVersion(unittest.TestCase):
    """Test get_version."""

    class MockedSubprocess(object):
        """Mocked Popen call."""
        def __init__(self, *args, **kwargs):
            """...."""
            self.args = args
            self.kwargs = kwargs

            if '--abbrev=0' in self.args:
                self.stdout = 'v1.2.3'
            else:
                self.stdout = 'v1.2.3+g1234567'

        def wait(self):
            pass

        def communicate(self):
            return ('v1.2.3+g1234567', '')

    @mock.patch('bin.get_version.subprocess')
    def test_get_version_run_full(self, mock_subprocess):
        """Test get_version call to git."""
        mock_subprocess.run = self.MockedSubprocess
        version = get_version.get_version()
        self.assertEqual(version, '1.2.3+g1234567')

    @mock.patch('bin.get_version.subprocess')
    def test_get_version_popen_full(self, mock_subprocess):
        """Test get_version call to git."""
        mock_subprocess.run = MagicMock(side_effect=AttributeError())
        mock_subprocess.Popen = self.MockedSubprocess
        version = get_version.get_version()
        self.assertEqual(version, '1.2.3+g1234567')
