import unittest

from main import addition

class testmain(unittest.TestCase):
    def test_add(self):
        assert addition(3, 4) == 7
        assert addition(-1, 1) == 0