class Luhn:

    def __init__(self, number):
        self.number = list(map(int, list(str(number))))

    def addends(self):
        temp = self.number[:]
        for idx in range(len(self.number) - 2, -1, -2):
            temp[idx] *= 2
            if temp[idx] >= 10:
                temp[idx] -= 9
        return temp

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return self.checksum() % 10 == 0 and len(self.number) > 1 and ''.join(map(str, self.number)).isdigit()

    def create(number):
        created = Luhn(number)
        created.number += [0]
        missingNum = 10 - created.checksum() % 10
        if missingNum == 10:
            return int(''.join(map(str, created.number)))
        else:
            return int(''.join(map(str, created.number[:-1] + [missingNum])))
