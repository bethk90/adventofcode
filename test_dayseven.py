import unittest
from unittest import TestCase
from dayseven import sum_directories

test_input = open('testinput_dayseven.txt').readlines()

test_output = 95437


class Test(TestCase):
    def test_sum_directories(self):
        self.assertEqual(sum_directories(test_input),test_output)


if __name__ == '__main__':
    unittest.main()
