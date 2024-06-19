import unittest
from flask_demo_helper.module7 import function7


class TestModule7(unittest.TestCase):
    def test_function7(self):
        self.assertEqual(function7(), "contents of all HTML documents")


if __name__ == '__main__':
    unittest.main()
