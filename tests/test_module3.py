import unittest
from flask_help_tools.module3 import function3


class TestModule3(unittest.TestCase):
    def test_function3(self):
        self.assertEqual(function3(), "contents of the models.py file")


if __name__ == '__main__':
    unittest.main()
