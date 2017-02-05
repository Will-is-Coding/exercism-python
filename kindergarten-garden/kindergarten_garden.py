from collections import OrderedDict

class Garden:

    children = {
        "Alice": [],
        "Bob": [],
        "Charlie": [],
        "David": [],
        "Eve": [],
        "Fred": [],
        "Ginny": [],
        "Harriet": [],
        "Ileana": [],
        "Joseph": [],
        "Kincaid": [],
        "Larry": []
    }

    plantTypes = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, plants):
        self.children = OrderedDict(sorted(self.children.items()))
        self.plantRows = plants.splitlines()
        self.plantRows = [row[i:i + 2] for row in self.plantRows for i in range(0, len(row), 2)]
        print(self.plantRows)

    def plants(self, student):
        return self.children[student]

    def assignPlants(self):
        #for cupIdx in range(len(self.plantRows[0])):
        pass

x = Garden("VVCCGG\nVVCCGG")
