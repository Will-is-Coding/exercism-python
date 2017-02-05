from math import sqrt


def sieve(num):

    flaggedNums = {i: True for i in range(2, num + 1)}

    for y in range(2, int(sqrt(num) + 1)):
        if flaggedNums[y]:
            for x in range(y**2, num + 1, y):
                flaggedNums[x] = False

    return list(filter(flaggedNums.get, flaggedNums))
