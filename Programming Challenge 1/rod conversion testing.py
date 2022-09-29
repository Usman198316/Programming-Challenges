import unittest

from Rod_Conversions import *


class MyFirstTest(unittest.TestCase):

    def converter(self):
        self.assertEqual(converter(10), "You would like to use a distance of 10.0 in rods. >50.292 in metres  >165.0 in Feet  >0.03125 in miles  >0.25 in Furlongs  It will take 0.6048387096774194 minutes to walk this distance")


if __name__ == '__main__':
    unittest.main()
