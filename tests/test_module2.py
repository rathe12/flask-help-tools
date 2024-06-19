import unittest
from flask_help_tools.module2 import function2


class TestModule2(unittest.TestCase):
    def test_function2(self):
        self.assertEqual(function2(), "contents of the forms.py file")


if __name__ == '__main__':
    unittest.main()
