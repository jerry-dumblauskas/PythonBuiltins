from unittest import TestCase
from puzzlers.check_for_leap import is_leap_year


class TestIsLeapYear(TestCase):
    def test_is_leap_year_100(self):
        year = 1900
        self.assertFalse(is_leap_year(year))

    def test_is_leap_year_normal(self):
        year = 1976
        self.assertTrue(is_leap_year(year))

    def test_is_leap_year_normal_false(self):
        year = 1998
        self.assertFalse(is_leap_year(year))

    def test_is_leap_year_400(self):
        year = 2000
        self.assertTrue(is_leap_year(year))
