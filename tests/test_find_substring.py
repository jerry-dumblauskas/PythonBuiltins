from unittest import TestCase
from boyer_moore import find_substring


class TestFindSubstring(TestCase):
    def test_find_substring(self):
        assert(find_substring("jad", "44jad") == 2)

class TestFindSubstring_long_item(TestCase):
    def test_find_substring(self):
        assert(find_substring("111109111",
                              "671111091113298117115999711432117110973297103117106973210111032117110321129710697114")
               == 2)