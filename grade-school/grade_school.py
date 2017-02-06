class School:

    schoolRoster = {}

    def __init__(self, name="Python School"):
        self.name = name

    def add(self, student, gradeLevel):
        if gradeLevel in self.schoolRoster.keys():
            self.schoolRoster[gradeLevel].append(student)
        else:
            self.schoolRoster[gradeLevel] = [student]

    def grade(self, gradeLevel):
        if gradeLevel in self.schoolRoster.keys():
            return self.schoolRoster[gradeLevel]
        else:
            return ()

    def sort(self):
        for gradeLevel in self.schoolRoster.keys():
            self.schoolRoster[gradeLevel] = tuple(sorted(self.schoolRoster[gradeLevel]))
        return self.schoolRoster

    def __reversed__(self):
        for grade in sorted(self.schoolRoster.keys(), reverse=True):
            yield grade, self.schoolRoster[grade]
