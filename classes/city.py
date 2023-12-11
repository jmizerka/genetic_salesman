import random


#  generate city with random coordinates
class City:
    def __init__(self):
        self.coor = (random.uniform(0, 1000), random.uniform(0, 1000))

    def __str__(self):
        return f" City's coordinates are: {self.coor}"
