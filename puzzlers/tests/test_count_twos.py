from unittest import TestCase
from puzzlers.count_numbers_in_num import count_twos

__author__ = 'jerrydumblauskas'


class TestCountTwos(TestCase):
    def test_count_twos(self):
        self.assertEqual(9, count_twos(25))
