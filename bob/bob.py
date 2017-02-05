def hey(what):
    """Responses of Bob, the lackadaisical teenager."""
    if what.isupper():
        return 'Whoa, chill out!'
    elif what.rstrip().endswith('?'):
        return 'Sure.'
    elif not what or what.isspace():
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
