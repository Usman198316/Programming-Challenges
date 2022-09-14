import unittest

from Richter import *


class MyFirstTest(unittest.TestCase):

    def test_convJoules(self):
        self.assertEqual(convJoules(3.4), 7943282347.242789)


if __name__ == '__main__':
    unittest.main()
