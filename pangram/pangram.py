import re


def is_pangram(posPangram):
    """Checks if a string is a pangram"""
    lenOfAlphabet = 26

    """Use regular expression to remove all non-alphabetic characters"""
    pattern = re.compile('[^a-zA-Z]')

    """Put into a set to remove all duplicate letters"""
    posPangram = set(pattern.sub('', posPangram).lower())

    if len(posPangram) == lenOfAlphabet:
        alpha = set('abcdefghijklmnopqrstuvwxyz')
        return set(posPangram).issubset(alpha)
    else:
        return False
