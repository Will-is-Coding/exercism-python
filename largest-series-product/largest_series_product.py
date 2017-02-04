from functools import reduce


def largest_product(num, seriesSize):
    if num and num.isdigit() and seriesSize > 0:
        numList = [int(n) for n in str(num)]
        return max([reduce((lambda x, y: x * y), numList[i:i + seriesSize]) for i, n in enumerate(numList) if i + seriesSize <= len(numList)])
    elif seriesSize == 0:
        return 1
    else:
        raise ValueError
