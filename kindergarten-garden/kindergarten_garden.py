class Garden:

    children = (
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry"
    )

    plantTypes = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, plants, students=[]):
        self.plantRows = [list(row) for row in plants.splitlines()]
        if students:
            self.children = sorted(students)
        self.assignPlants()

    def plants(self, student):
        return self.children[student]

    def assignPlants(self):
        plantsGrouped = [self.plantRows[0][i:i + 2] + self.plantRows[1][i:i + 2] for i in range(0, len(self.plantRows[0]), 2)]
        self.children = dict(zip(self.children, plantsGrouped))
        for child in self.children.keys():
            self.children[child] = [self.plantTypes[plant] for plant in self.children[child]]
