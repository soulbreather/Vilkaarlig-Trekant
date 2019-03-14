def CosRelVinkelA(side1, side2, side3):
    import math
    vinkel1 = math.acos((side1**2 - side2**2 - side3**2)/(-2 * side2 * side3))

    vinkel1 = math.degrees(vinkel1)

    return vinkel1


def CosRelVinkelB(side1, side2, side3):
    import math
    vinkel2 = math.acos((side2**2 - side1**2 - side3**2)/(-2 * side1 * side3))

    vinkel2 = math.degrees(vinkel2)

    return vinkel2


def CosRelVinkelC(side1, side2, side3):
    import math
    vinkel3 = math.acos((side3**2 - side1**2 - side2**2)/(-2 * side1 * side2))

    vinkel3 = math.degrees(vinkel3)

    return vinkel3
