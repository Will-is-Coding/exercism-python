from operator import itemgetter

def numeral(num):
    numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    romanNumerals = ''
    for numeral in sorted(numerals.items(), key=itemgetter(1), reverse=True):
        while num >= numeral[1]:
            romanNumerals += numeral[0]
            num -= numeral[1]
    return romanNumerals