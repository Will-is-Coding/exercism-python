class Clock(object):
    """Clock that represents time within a 24 hour period, with no AM or PM.

    Attributes:
        minInhour(integer): 60 minutes in on hour
        hourInDay(integer): 24 hours in a day
    """

    minInHour = 60
    hourInDay = 24

    def __init__(self, hour, minute):
        """Initiate clock with an hour and minute

        Args:
            hour(integer): Given hour
            minute(integer): Given minute

        Note:
            Automatically formats the time with formatTime()

        """
        self.hour = hour
        self.minute = minute
        self.formatTime()

    def __str__(self):
        """Returns formatted time"""
        return self.time

    def __eq__(self, other):
        """Returns if the formatted time properties are equal"""
        return self.time == other.time

    def formatHour(self):
        """Set clock's hour to be within 24 hours"""
        self.hour %= self.hourInDay

    def formatMin(self):
        """Set clock's minute to be within 60 minutes. Add surplus to hours"""
        self.hour += self.minute // self.minInHour
        self.minute %= self.minInHour

    def formatTime(self):
        """Format time in HH:MM string"""
        self.formatMin()
        self.formatHour()
        self.time = '{:02}:{:02}'.format(self.hour, self.minute)

    def add(self, minute):
        """Add minutes to the clock, reformats time"""
        self.minute += minute
        self.formatTime()
        return self.time
