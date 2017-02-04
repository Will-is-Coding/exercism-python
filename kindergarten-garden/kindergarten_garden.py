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

    plantTypes = (
        "Grass",
        "Clover",
        "Radishes",
        "Violets"
    )

    def __init__(self, plants):
        self.children = OrderedDict(sorted(self.children.items()))
        self.plantRows = plants.splitlines()
        print(self.plantRows)
        print(self.children)

x = Garden("VVCCGG\nVVCCGG")
