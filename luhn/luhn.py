import re

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
        print(self.number)
        return self.checksum() % 10 == 0 and len(self.number) > 1 and ''.join(map(str, self.number)).isdigit()

    def create(self, number):
        self.number = number
        if checksum() % 10 != 0:
            return self.addends() + [checksum() % 10]
        else:
            return self.addends()

print(Luhn.create(837263756))
