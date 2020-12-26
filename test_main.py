import unittest
import main


class TestCap(unittest.TestCase):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def test_shuffled_list(self):
        result = main.shuffle(self.lst[:], 3)
        self.assertNotEqual(result[0], self.lst[0])
        self.assertNotEqual(result[1], self.lst[1])
        self.assertNotEqual(result[2], self.lst[2])

    def test_original_list_changes(self):
        lst = self.lst[:]
        result = main.shuffle(lst, 3)
        self.assertEqual(result[0], lst[0])
        self.assertEqual(result[1], lst[1])
        self.assertEqual(result[2], lst[2])


if __name__ == '__main__':
    unittest.main()
