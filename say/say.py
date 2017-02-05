numberPhonetics = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'sevnety',
    80: 'eighty',
    90: 'ninety'
}

amountPhonetics = [
    "",
    "thousand",
    "million",
    "billion"
]


def breakHundred(num, last=False):
    toSay = ''
    if num >= 100:
        toSay = belowHundred(num // 100, toSay).rstrip() + ' hundred '
        if num % 100 != 0:
            if last:
                toSay += 'and '
            return belowHundred(num % 100, toSay)
    else:
        if last:
            toSay += 'and '
        toSay = belowHundred(num, toSay)

    return toSay.rstrip()


def belowHundred(num, toSay):
    if 0 < num < 20:
        toSay += numberPhonetics[num] + ' '
    elif num % 10 == 0:
        toSay += numberPhonetics[num] + ' '
    else:
        toSay += numberPhonetics[num - num % 10] + '-' + numberPhonetics[num % 10]

    return toSay


def say(num):
    num = int(num)
    if num == 0:
        return 'zero'
    elif 0 < num < 1e12:
        numGroups = list(map(int,format(num, ',').split(',')))
        numGroups.reverse()
        phoneticGroups = [item for item in zip(numGroups, amountPhonetics)]
        phoneticPhrase = []

        for group in phoneticGroups:
            if group[0]:
                phoneticPhrase.append(
                    breakHundred(
                        group[0],
                        (
                            group[0] > 100
                        ) or
                        (
                            group == phoneticGroups[0] and
                            len(phoneticGroups) > 1 and
                            group[0] < 100
                        )
                    ) + ' ' + group[1]
                )

        phoneticPhrase.reverse()
        return ' '.join(phoneticPhrase).rstrip()

    else:
        raise AttributeError('Out of range')
