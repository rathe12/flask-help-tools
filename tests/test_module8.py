import unittest
from flask_demo_helper.module8 import function8


class TestModule8(unittest.TestCase):
    def test_function8(self):
        self.assertEqual(function8(), "contents of the styles.css file")


if __name__ == '__main__':
    unittest.main()
