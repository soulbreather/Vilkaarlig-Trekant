import math


def CosRelSide(side1, side2, vinkelMellemSider):
    return math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(math.radians(vinkelMellemSider)))
