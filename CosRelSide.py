import math


def CosRelSide(side1, side2, vinkel1):
    return math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(math.radians(vinkel1)))
