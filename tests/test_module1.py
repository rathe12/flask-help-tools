import unittest
from flask_help_tools.module1 import function1


class TestModule1(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(function1(), "contents of the routes.py file")


if __name__ == '__main__':
    unittest.main()
