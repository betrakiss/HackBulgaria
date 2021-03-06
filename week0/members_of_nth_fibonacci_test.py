import unittest
from member_of_nth_fibonacci_lists import member_of_nth_fibonacci_lists


class MembersOfNthFibonacciTest(unittest.TestCase):

    def test_lines(self):
        self.assertFalse(member_of_nth_fibonacci_lists([1, 2], [3, 4], [5, 6]))
        self.assertFalse(member_of_nth_fibonacci_lists([7, 11], [2], [11, 7, 2, 2, 7]))
        self.assertTrue(member_of_nth_fibonacci_lists([1, 2], [3, 4],
                                                      [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
        self.assertTrue(member_of_nth_fibonacci_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))


if __name__ == '__main__':
    unittest.main()
