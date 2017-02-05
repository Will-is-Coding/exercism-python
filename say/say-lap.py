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
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    1000000: 'million',
    1000000000: 'billion'
}

ten = 10
hundred = ten**2
thou = hundred * ten
mill = thou**2
bill = thou**3
trill = thou**4


def say(num):
    toSay = ''
    if num == 0:
        return 'zero'

    if 1000000000 <= num < 1000000000000:
        if num // 1000000000 != 0:
            toSay += numberPhonetics[num // 1000000000] + ' '
        toSay += numberPhonetics[1000000000] + ' '
        num -= num - (num % 1000000000)

    if 1000000 <= num < 1000000000:
        if num // 1000000 != 0:
            toSay += numberPhonetics[num // 1000000] + ' '
        toSay += numberPhonetics[1000000] + ' '
        num -= num - (num % 1000000)

    if 1000 <= num < 1000000:
        if num // 1000 != 0:
            toSay += numberPhonetics[num // 1000] + ' '
        toSay += numberPhonetics[1000] + ' '
        num -= num - (num % 1000)

    if 100 <= num < 1000:
        if num // 100 != 0:
            toSay += numberPhonetics[num // 100] + ' '
        toSay += numberPhonetics[100] + ' '
        num -= num - (num % 100)

    if 0 < num < 100:
        if toSay:
            toSay += 'and '
        if num < 20:
            toSay += numberPhonetics[num] + ' '
        elif num % 10 == 0:
            toSay += numberPhonetics[num] + ' '
        else:
            toSay += numberPhonetics[num - num % 10] + '-' + numberPhonetics[num % 10]

    print(toSay)
    #else:
        #raise AttributeError('Number out of range')
        #

def belowHundred(num, toSay):
    if num < 20:
        toSay += numberPhonetics[num] + ' '
    elif num % 10 == 0:
        toSay += numberPhonetics[num] + ' '
    else:
        toSay += numberPhonetics[num - num % 10] + '-' + numberPhonetics[num % 10]

    print(toSay)


def intoThousands(num):
    print( num % 1000 )

intoThousands(1001)

def say2(num):
    num = str(num).zfill(3)
    print(num)

