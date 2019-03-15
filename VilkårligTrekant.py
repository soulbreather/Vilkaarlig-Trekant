import math


def CosRelSide(side1, side2, vinkelMellemSider):
    side3 = math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(math.radians(vinkelMellemSider)))
    return side3


def CosRelVinkelA(side1, side2, side3):
    vinkel1 = math.acos((side1**2 - side2**2 - side3**2)/(-2 * side2 * side3))

    vinkel1 = math.degrees(vinkel1)

    return vinkel1


def CosRelVinkelB(side1, side2, side3):
    vinkel2 = math.acos((side2**2 - side1**2 - side3**2)/(-2 * side1 * side3))

    vinkel2 = math.degrees(vinkel2)

    return vinkel2


def CosRelVinkelC(side1, side2, side3):
    vinkel3 = math.acos((side3**2 - side1**2 - side2**2)/(-2 * side1 * side2))

    vinkel3 = math.degrees(vinkel3)

    return vinkel3


def SinRelSide(side1, vinkel1, vinkel2):
    side2 = (side1 * math.sin(math.radians(vinkel2))) / math.sin((math.radians(vinkel1)))
    return side2


def SinRelVinkel(side1, side2, vinkel1):
    vinkel2Sin = (math.sin(math.radians(vinkel1))*side2) / side1
    vinkel2asin = math.asin(vinkel2Sin)
    vinkel2 = math.degrees(vinkel2asin)
    return vinkel2


def Sum180(vinkel, vinkel2):
    vinkel3 = 180 - vinkel - vinkel2
    return vinkel3


def Picker(a, b, c, A, B, C):
    print("")
    if (a != 0 and b != 0 and c != 0):
        A = CosRelVinkelA(a, b, c)
        B = CosRelVinkelA(b, a, c)
        C = CosRelVinkelA(c, a, b)

    elif (a != 0 and b != 0 and A != 0):
        B = SinRelVinkel(a, b, A)
        C = Sum180(A, B)
        c = SinRelSide(a, A, C)

    elif (a != 0 and b != 0 and B != 0):
        A = SinRelVinkel(a, b, B)
        C = Sum180(A, B)
        c = SinRelSide(a, A, C)

    elif (a != 0 and b != 0 and C != 0):
        c = CosRelSide(a, b, C)
        A = CosRelVinkelA(a, b, c)
        B = CosRelVinkelB(a, b, c)

    elif (b != 0 and c != 0 and A != 0):
        a = CosRelSide(b, c, A)
        B = CosRelVinkelB(a, b, c)
        C = CosRelVinkelC(a, b, c)

    elif (b != 0 and c != 0 and B != 0):
        C = SinRelVinkel(b, c, B)
        A = Sum180(B, C)
        a = SinRelSide(b, B, A)

    elif (b != 0 and c != 0 and C != 0):
        B = SinRelVinkel(b, c, C)
        A = Sum180(B, C)
        a = SinRelSide(b, B, A)

    elif (a != 0 and c != 0 and A != 0):
        C = SinRelVinkel(a, c, A)
        B = Sum180(A, C)
        b = SinRelSide(a, A, B)

    elif (a != 0 and c != 0 and B != 0):
        b = CosRelSide(a, c, B)
        A = CosRelVinkelA(a, b, c)
        C = CosRelVinkelC(c, a, b)

    elif (a != 0 and c != 0 and C != 0):
        A = SinRelVinkel(a, c, C)
        B = Sum180(A, C)
        b = SinRelSide(a, A, B)

    elif (a != 0 and A != 0 and B != 0):
        b = SinRelSide(a, A, B)
        C = Sum180(A, B)
        c = SinRelSide(b, B, C)

    elif (b != 0 and A != 0 and B != 0):
        a = SinRelSide(b, B, A)
        C = Sum180(A, B)
        c = SinRelSide(b, B, C)

    elif (c != 0 and A != 0 and B != 0):
        C = Sum180(A, B)
        a = SinRelSide(c, C, A)
        b = SinRelSide(c, C, B)

    elif (a != 0 and B != 0 and C != 0):
        A = Sum180(B, C)
        b = SinRelSide(a, A, B)
        c = SinRelSide(a, A, C)

    elif (b != 0 and B != 0 and C != 0):
        A = Sum180(B, C)
        c = SinRelSide(b, B, C)
        a = SinRelSide(c, C, A)

    elif (c != 0 and B != 0 and C != 0):
        A = Sum180(B, C)
        a = SinRelSide(c, C, A)
        b = SinRelSide(c, C, B)

    elif (a != 0 and A != 0 and C != 0):
        B = Sum180(A, C)
        b = SinRelSide(a, A, B)
        c = SinRelSide(a, A, C)

    elif (b != 0 and A != 0 and C != 0):
        B = Sum180(A, C)
        a = SinRelSide(b, B, A)
        c = SinRelSide(b, B, C)

    elif (c != 0 and A != 0 and C != 0):
        B = Sum180(A, C)
        b = SinRelSide(c, C, B)
        a = SinRelSide(c, C, A)

    else:
        print("Trekanten kan ikke løses sådan.")

    vilkårligTrekant = ""
    trekant = print("a = " + str(a)), print("b = " + str(b)), print("c = " + str(c)
                                                                    ), print("A = " + str(A)), print("B = " + str(B)), print("C = " + str(C))
    trekant = vilkårligTrekant

    return vilkårligTrekant
