from unittest import TestCase
from skyline import calc_skyline2
__author__ = 'jerrydumblauskas'


class TestTester(TestCase):
    def test_tester(self):
        self.assertEqual(
            calc_skyline2([(1,11,5),(2,6,7),(3,13,9),(12,7,16),(14,3,25),(19,18,22),(23,13,29),(24,4,28)]),
            ((1,11,3,13,9,0,12,7,16,3,19,18,22,3,23,13,29,0)) )