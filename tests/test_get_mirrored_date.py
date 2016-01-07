from solstice_balance import get_solstice_date
import datetime
from unittest import TestCase
from freezegun import freeze_time


class TestGet_mirror_date(TestCase):
    @freeze_time("2015-12-21")
    def test_get_mirror_date_on_solstice_day(self):
        self.assertEqual(get_solstice_date(), datetime.date(2015, 12, 21))

    @freeze_time("2016-2-21")
    def test_get_mirror_date_before_equinox_day(self):
        self.assertEqual(get_solstice_date(), datetime.date(2015, 12, 21) )

    @freeze_time("2016-5-21")
    def test_get_mirror_date_after_equinox_day(self):
        self.assertEqual(get_solstice_date(), datetime.date(2016, 6, 21) )

