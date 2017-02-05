import re
from collections import Counter


def word_count(string):
    """Count the instances of each word in a string and
    return each word with its count"""
    string = string.lower()
    words = re.findall('[^\W_]+', string, re.I)
    return Counter(words)
