NORTH, EAST, SOUTH, WEST = ((0, 1), (1, 0), (0, -1), (-1, 0))


class Robot:
    """Robot simulator that has coordinates, bearing, and can advance

    Variables:
        directions {list} -- Cardinal directions in a list
        coordinates {tuple} -- Contains x, y coordinates
        bearing {tuple} -- Contains the current bearing
    """

    directions = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, direction=NORTH, x=0, y=0):
        """Set up the robot with a direction and coordinates

        Keyword Arguments:
            direction {[type]} -- (default: {NORTH})
            x {number} -- (default: {0})
            y {number} -- (default: {0})
        """
        self.coordinates = (x, y)
        self.bearing = direction

    def simulate(self, instructions):
        """Given a string, no spaces, discern actions to take

        The letter-string "RAALAL" means:
        - Turn right
        - Advance twice
        - Turn left
        - Advance once
        - Turn left yet again

        Arguments:
            instructions {[type]} -- String containg only A, L, or R - no spaces
        """
        for letter in instructions:
            if letter == "A":
                self.advance()
            elif letter == "R":
                self.turn_right()
            elif letter == "L":
                self.turn_left()

    def advance(self):
        """Advance one step at current bearing"""
        self.coordinates = tuple(sum(coord) for coord in zip(self.bearing, self.coordinates))

    def turn_right(self):
        """Turn right of current bearing"""
        self.bearing = self.directions[(self.directions.index(self.bearing) + 1) % len(self.directions)]

    def turn_left(self):
        """Turn left of currrent bearing"""
        self.bearing = self.directions[(self.directions.index(self.bearing) - 1) % len(self.directions)]
