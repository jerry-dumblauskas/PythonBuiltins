import datetime

the_day = datetime.date(1901, 1, 1)
add_a_day = datetime.timedelta(days=1)
cnt = 0
while True:
    if the_day.weekday() == 6 and the_day.day == 1:
        cnt += 1

    if the_day.year == 2000 and the_day.month == 12 and the_day.day == 31:
        break
    the_day = the_day + add_a_day
print(cnt)

