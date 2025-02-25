class Hole:
    def __init__(self, radius, x, y):
        """
        Hole defined by:
        :param x: x dimension for center point of the circle as a ratio of letter height
        :param y: y dimension for center point of the circle as a ratio of letter height
        :param radius: radius of circle as a ratio of letter height
        """
        self.x = x
        self.y = y
        self.radius = radius


A = [Hole(1/12, 1/2, 7/12)]
B = [Hole(1/12, 1/2, 3/4), Hole(1/12, 1/2, 1/4)]
D = [Hole(1/3, 1/2, 1/2)]
P = [Hole(1/12, 1/2, 3/4)]