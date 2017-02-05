class Allergies:

    allergens = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats"
    ]

    def __init__(self, allergyCount):
        self.allergyCount = allergyCount
        self.lst = []
        self.findAllergens()

    def findAllergens(self):
        for i, k in enumerate(self.allergens):
            if self.allergyCount & 1 << i:
                self.lst.append(k)
        return self.lst

    def is_allergic_to(self, allergen):
        return allergen in self.lst
