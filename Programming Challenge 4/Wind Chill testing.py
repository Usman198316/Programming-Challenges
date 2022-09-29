import unittest

from Wind_Chill import *


class MyFirstTest(unittest.TestCase):

    def WCTcalc(self):
        self.assertEqual(WCTcalc(10, 15), -6.5895344209562525)


if __name__ == '__main__':
    unittest.main()
