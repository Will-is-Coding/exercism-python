class SpaceAge:
    earthYearInSeconds = 31557600

    def __init__(self, seconds):
        self.seconds = seconds
        self.earthAge = self.seconds / self.earthYearInSeconds

    def on_mercury(self):
        mercuryYearRatio = 0.2408467
        return round(self.earthAge / mercuryYearRatio, 2)

    def on_venus(self):
        venusYearRatio = 0.61519726
        return round(self.earthAge / venusYearRatio, 2)

    def on_earth(self):
        return round(self.earthAge, 2)

    def on_mars(self):
        marsYearRatio = 1.8808158
        return round(self.earthAge / marsYearRatio, 2)

    def on_jupiter(self):
        jupiterYearRatio = 11.862615
        return round(self.earthAge / jupiterYearRatio, 2)

    def on_saturn(self):
        saturnYearRatio = 29.447498
        return round(self.earthAge / saturnYearRatio, 2)

    def on_uranus(self):
        uranusYearRatio = 84.016846
        return round(self.earthAge / uranusYearRatio, 2)

    def on_neptune(self):
        neptuneYearRatio = 164.79132
        return round(self.earthAge / neptuneYearRatio, 2)
