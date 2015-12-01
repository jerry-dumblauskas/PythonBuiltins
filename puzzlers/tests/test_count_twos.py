__author__ = 'jerrydumblauskas'

from unittest import TestCase

from puzzlers.count_numbers_in_num import count_twos


class TestcountTwos(TestCase):
    def test_count_twos(self):
        self.assertEqual(9, count_twos(25))
