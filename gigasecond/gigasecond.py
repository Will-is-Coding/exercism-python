import datetime


def add_gigasecond(date):
    """Add a gigasecond to a datetime object and return the new datetime object"""
    gigasecond = 1000000000
    return date + datetime.timedelta(seconds=gigasecond)
