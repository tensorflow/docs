import unittest
import subprocess
import datetime

from setup import get_version

class TestSetup(unittest.TestCase):
    def test_get_version(self):
        ts = int(
            subprocess.check_output(['git', 'log', '-1', '--format=%ct', 'tools'])
            .decode('utf-8')
            .strip()
        )
        self.assertIsInstance(ts, int)

    def test_get_version_format(self):
        version = get_version()
        self.assertRegex(version, r'^\d{4}\.\d{2}\.\d{2}\.\d+$')

    def test_get_version_date(self):
        version = get_version()
        parts = version.split('.')
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        self.assertTrue(2000 <= year <= datetime.datetime.now().year)
        self.assertTrue(1 <= month <= 12)
        self.assertTrue(1 <= day <= 31)

    def test_get_version_seconds(self):
        version = get_version()
        parts = version.split('.')
        seconds = int(parts[3])
        self.assertTrue(0 <= seconds < 86400)

    def test_get_version_not_empty(self):
        version = get_version()
        self.assertTrue(len(version) > 0)

if __name__ == '__main__':
    unittest.main()
        self.assertIsInstance(ts, int)

    def test_get_version_format(self):
        version = get_version()
        self.assertRegex(version, r'^\d{4}\.\d{2}\.\d{2}\.\d+$')

    def test_get_version_date(self):
        version = get_version()
        parts = version.split('.')
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        self.assertTrue(2000 <= year <= datetime.datetime.now().year)
        self.assertTrue(1 <= month <= 12)
        self.assertTrue(1 <= day <= 31)

if __name__ == '__main__':
    unittest.main()
        self.assertIsInstance(ts, int)

if __name__ == '__main__':
    unittest.main()