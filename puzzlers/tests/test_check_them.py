from puzzlers.anagrams import check_them
from unittest import TestCase

__author__ = 'jerrydumblauskas'


class TestCheckThem(TestCase):
    def test_check_them_equals(self):
        self.assertEqual(True, check_them('poppy goes home', 'home goes poppy'))

    def test_check_them_not_an_anagram_diff_length(self):
        self.assertEqual(False, check_them('pp', 'opp'))

    def test_check_them_not_an_anagram_same_length(self):
        self.assertEqual(False, check_them('pep', 'opp'))
