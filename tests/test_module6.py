import unittest
from flask_demo_helper.module6 import function6


class TestModule6(unittest.TestCase):
    def test_function6(self):
        self.assertEqual(function6(), "contents of the run.py file")


if __name__ == '__main__':
    unittest.main()
