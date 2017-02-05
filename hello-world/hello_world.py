def hello(name=''):
	'''
	Return a greeting to the name provided. If no valid name is given, simply return 'Hello, World!'
	'''
	if name != '' and name is not None:
		return 'Hello, ' + name + '!'
	else:
		return 'Hello, World!'