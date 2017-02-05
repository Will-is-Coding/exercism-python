def is_leap_year(year):
	'''
	Given a 4 digit year, return if it is a leap year
	'''
	if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
		return True
	elif year % 4 == 0 and year % 100 != 0:
		return True
	else:
		return False