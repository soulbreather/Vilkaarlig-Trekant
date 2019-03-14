def SinRelVinkel(side1, side2, vinkel1):
    import math
    vinkel2Sin = (math.sin(math.radians(vinkel1))*side2) / side1
    vinkel2 = math.asin(vinkel2Sin)
    return math.degrees(vinkel2)




