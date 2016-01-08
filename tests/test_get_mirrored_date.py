from solstice_balance import get_solstice_date, get_mirror_date
import datetime
from unittest import TestCase
from freezegun import freeze_time


class TestGet_solstice_date(TestCase):
    @freeze_time("2015-12-21")
    def test_get_solstice_date_on_solstice_day(self):
        self.assertEqual(get_solstice_date(), datetime.date(2015, 12, 21))

    @freeze_time("2016-2-21")
    def test_get_solstice_date_before_equinox_day(self):
        self.assertEqual(get_solstice_date(), datetime.date(2015, 12, 21) )

    @freeze_time("2016-5-21")
    def test_get_solstice_date_after_equinox_day(self):
        self.assertEqual(get_solstice_date(), datetime.date(2016, 6, 21) )

class TestGet_mirror_date(TestCase):
    @freeze_time("2015-12-21")
    def test_get_mirror_date_on_solstice_day(self):
        self.assertEqual(get_mirror_date(), datetime.date(2015, 12, 21))

    @freeze_time("2016-2-21")
    def test_get_mirror_date_before_equinox_day(self):
        self.assertEqual(get_mirror_date(), datetime.date(2015, 10, 20) )

    @freeze_time("2016-5-21")
    def test_get_mirror_date_after_equinox_day(self):
        self.assertEqual(get_mirror_date(), datetime.date(2016, 7, 22) )

    @freeze_time("2016-12-22")
    def test_get_mirror_date_simple_1(self):
        self.assertEqual(get_mirror_date(), datetime.date(2016, 12, 20) )

    @freeze_time("2015-12-31")
    def test_get_mirror_date_simple_2(self):
        self.assertEqual(get_mirror_date(), datetime.date(2015, 12, 11) )
