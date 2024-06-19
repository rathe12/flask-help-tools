import unittest
from flask_help_tools.module9 import function9


class TestModule9(unittest.TestCase):
    def test_function9(self):
        self.assertEqual(function9(), "project structure")


if __name__ == '__main__':
    unittest.main()
