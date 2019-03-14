# Dette program udregner vha. sinusrelationen den manglende vinkel
import math


def SinRelSide(side1, vinkel1, vinkel2):
    side2 = (side1 * math.sin(math.radians(vinkel2))) / math.sin((math.radians(vinkel1)))
    return side2
