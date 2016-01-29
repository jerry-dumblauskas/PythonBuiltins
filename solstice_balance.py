"""
This module will be used to check the expected daylight hours on a day and
return the day that most closest matches this day.

for example, the winter solstice is usually on 12/21 -- so on 12/28 the daylight hours
are the same as 12/14.


also, we want to compare to the nearest solstice -- Feb 21rst would compare back
October 21rst 'ish' whereas april 21rst should compare to a date in August

Just learned that the winter solstice is not always on 12/21, but sometimes on
12/22 -- don't want an internet connection to make this work, so I'll either find a formula, or
get the next 10 years of data and store it in here

"""

import datetime


def _get_solstice_date():
    """
    method that provides the solstice date to use -- internal for now!
    :return: date
    """
    today_date = datetime.datetime.now().date()
    today_year = today_date.year
    june_solstice = datetime.date(today_year, 6, 21)
    december_solstice = datetime.date(today_year, 12, 21)
    last_december_solstice = datetime.date(today_year - 1, 12, 21)

    # edge cases -- either solstice dates return itself
    if today_date == june_solstice:
        return june_solstice
    if today_date == december_solstice:
        return december_solstice

    pivot_date = june_solstice
    time_delta = today_date - june_solstice
    if time_delta.days < -91:
        pivot_date = last_december_solstice
    if time_delta.days > 91:
        pivot_date = december_solstice

    return pivot_date


def get_mirror_date():
    mirror_date = _get_solstice_date()
    return mirror_date - (datetime.datetime.now().date() - mirror_date)


if __name__ == "__main__":
    print(get_mirror_date())
