from datetime import date
import calendar


class MeetupDayException(Exception):
    pass

def meetup_day(year, month, day, suffix):
    """Return the next date of the meetup given the year, month, day name and suffix"""
    dayList = list(calendar.day_name)
    teenths = range(13, 20)
    dayInMonth = []

    for dayIdx in range(1, calendar.monthrange(year, month)[1] + 1):
        if calendar.weekday(year, month, dayIdx) == dayList.index(day):
            dayInMonth.append(dayIdx)

    try:
        if suffix == '1st':
            return date(year, month, dayInMonth[0])
        elif suffix == '2nd':
            return date(year, month, dayInMonth[1])
        elif suffix == '3rd':
            return date(year, month, dayInMonth[2])
        elif suffix == '4th':
            return date(year, month, dayInMonth[3])
        elif suffix == '5th':
            return date(year, month, dayInMonth[4])
        elif suffix == 'last':
            return date(year, month, dayInMonth.pop())
        else:
            return date(year, month, next(d for d in dayInMonth if d in teenths))
    except:
        raise MeetupDayException
