from binary_search import binary_search as bs
import unittest

class TestBinarySearch(unittest.TestCase):
    
    def test_for_100_list(self):
        lst = [x for x in range(1, 101)]
        self.assertEqual(bs(lst, 67), 66)
        self.assertEqual(bs(lst, 52), 51)

    def test_None(self):
        lst = [x for x in range(1, 101)]
        self.assertEqual(bs(lst, 666), None)

if __name__ == '__main__':
    unittest.main()