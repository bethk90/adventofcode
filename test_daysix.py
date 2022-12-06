from unittest import TestCase
from daysix import find_marker

test_one, test_two, test_three, test_four = [test for test in open('testinput_daysix.txt').readlines()]
output_one, output_two, output_three, output_four = [5,6,10,11]


class Test(TestCase):
    def test_find_marker_one(self):
        self.assertEqual(find_marker(test_one),output_one)

    def test_find_marker_two(self):
        self.assertEqual(find_marker(test_two),output_two)

    def test_find_marker_three(self):
        self.assertEqual(find_marker(test_three),output_three)

    def test_find_marker_four(self):
        self.assertEqual(find_marker(test_four),output_four)


if __name__ == '__main__':
    unittest.main()
