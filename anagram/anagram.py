def are_anagrams(gvnWord, toCheck):
    return sorted(gvnWord.lower()) == sorted(toCheck.lower()) and gvnWord.lower() != toCheck.lower()


def detect_anagrams(gvnWord, wordList):
    return [word for word in wordList if are_anagrams(gvnWord, word)]
