import unittest

from solution import solve


class ApiTest(unittest.TestCase):

    def test_success(self):
        self.assertTupleEqual(solve(4), (7, 15))
        self.assertTupleEqual(solve(0), (0, 0))

    def test_fail(self):
        self.assertEqual(solve('4'), 'Invalid value passed. Pass an integer')


if __name__ == '__main__':
    unittest.main()
