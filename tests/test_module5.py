import unittest
from flask_help_tools.module5 import function5


class TestModule5(unittest.TestCase):
    def test_function5(self):
        self.assertEqual(function5(), "contents of the config.py file")


if __name__ == '__main__':
    unittest.main()
