def SinRelVinkel(side1, side2, vinkel1):
    import math
    vinkel2Sin = (math.sin(math.radians(vinkel1))*side2) / side1
    vinkel2asin = math.asin(vinkel2Sin)
    vinkel2 = math.degrees(vinkel2asin)
    return vinkel2
