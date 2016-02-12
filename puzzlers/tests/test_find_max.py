from unittest import TestCase
from puzzlers.greatest_sum_in_a_list import find_max

__author__ = 'jerrydumblauskas'


class TestFindMax(TestCase):
    def test_find_max(self):
        """
        unit test to hit the main use case of the sum in a list problem
        """
        self.assertEqual(5, find_max([2, -8, 3, -2, 4, -10]))
