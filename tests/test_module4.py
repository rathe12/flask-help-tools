import unittest
from flask_demo_helper.module4 import function4


class TestModule4(unittest.TestCase):
    def test_function4(self):
        self.assertEqual(function4(), "contents of the __init__.py file")


if __name__ == '__main__':
    unittest.main()
