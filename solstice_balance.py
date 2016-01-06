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

def get_mirrored_date():
    """
    main method that provides the solstice 'mirror' date
    :return: date
    """
    today_date = datetime.datetime.now().date()

    return today_date