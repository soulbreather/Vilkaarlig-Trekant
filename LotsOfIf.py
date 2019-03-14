import CosRelSide
import CosRelVinkel
import SinRelSide
import SinRelVinkel
import Sum180


def Picker(a, b, c, A, B, C):
    if (a != 0 and b != 0 and c != 0):
        A = CosRelVinkel.CosRelVinkelA(a, b, c)
        B = CosRelVinkel.CosRelVinkelA(b, a, c)
        C = CosRelVinkel.CosRelVinkelA(c, a, b)

    elif (a != 0 and b != 0 and A != 0):
        B = SinRelVinkel.SinRelVinkel(a, b, A)
        C = Sum180.Sum180(A, B)
        c = SinRelSide.SinRelSide(a, A, C)

    elif (a != 0 and b != 0 and B != 0):
        A = SinRelVinkel.SinRelVinkel(a, b, B)
        C = Sum180.Sum180(A, B)
        c = SinRelSide.SinRelSide(a, A, C)

    elif (a != 0 and b != 0 and C != 0):
        c = CosRelSide.CosRelSide(a, b, C)
        A = CosRelVinkel.CosRelVinkelA(a, b, c)
        B = CosRelVinkel.CosRelVinkelB(a,b,c)

    elif (b != 0 and c != 0 and A != 0):
        a = CosRelSide.CosRelSide(b, c, A)
        B = CosRelVinkel.CosRelVinkelB(a, b, c)
        C = CosRelVinkel.CosRelVinkelC(a, b, c)

    elif (b != 0 and c != 0 and B != 0):
        C = SinRelVinkel.SinRelVinkel(b, c, B)
        A = Sum180.Sum180(B, C)
        a = SinRelSide.SinRelSide(b, B, A)

    elif (b != 0 and c != 0 and C != 0):
        B = SinRelVinkel.SinRelVinkel(b, c, C)
        A = Sum180.Sum180(B, C)
        a = SinRelSide.SinRelSide(b, B, A)

    elif (a != 0 and c != 0 and A != 0):
        C = SinRelVinkel.SinRelVinkel(a, c, A)
        B = Sum180.Sum180(A, C)
        b = SinRelSide.SinRelSide(a, A, B)

    elif (a != 0 and c != 0 and B != 0):
        b = CosRelSide.CosRelSide(a, c, B)
        A = CosRelVinkel.CosRelVinkelA(a, b, c)
        C = CosRelVinkel.CosRelVinkelC(c, a, b)

    elif (a != 0 and c != 0 and C != 0):
        A = SinRelVinkel.SinRelVinkel(a, c, C)
        B = Sum180.Sum180(A, C)
        b = SinRelSide.SinRelSide(a, A, B)

    elif (a != 0 and A != 0 and B != 0):
        b = SinRelSide.SinRelSide(a, A, B)
        C = Sum180.Sum180(A, B)
        c = SinRelSide.SinRelSide(b, B, C)

    elif (b != 0 and A != 0 and B != 0):
        a = SinRelSide.SinRelSide(b, B, A)
        C = Sum180.Sum180(A, B)
        c = SinRelSide.SinRelSide(b, B, C)

    elif (c != 0 and A != 0 and B != 0):
        C = Sum180.Sum180(A, B)
        a = SinRelSide.SinRelSide(c, C, A)
        b = SinRelSide.SinRelSide(c, C, B)

    elif (a != 0 and B != 0 and C != 0):
        A = Sum180.Sum180(B, C)
        b = SinRelSide.SinRelSide(a, A, B)
        c = SinRelSide.SinRelSide(a, A, C)

    elif (b != 0 and B != 0 and C != 0):
        A = Sum180.Sum180(B, C)
        c = SinRelSide.SinRelSide(b, B, C)
        a = SinRelSide.SinRelSide(c, C, A)

    elif (c != 0 and B != 0 and C != 0):
        A = Sum180.Sum180(B, C)
        a = SinRelSide.SinRelSide(c, C, A)
        b = SinRelSide.SinRelSide(c, C, B)

    elif (a != 0 and A != 0 and C != 0):
        B = Sum180.Sum180(A, C)
        b = SinRelSide.SinRelSide(a, A, B)
        c = SinRelSide.SinRelSide(a, A, C)

    elif (b != 0 and A != 0 and C != 0):
        B = Sum180.Sum180(A, C)
        a = SinRelSide.SinRelSide(b, B, A)
        c = SinRelSide.SinRelSide(b, B, C)

    elif (c != 0 and A != 0 and C != 0):
        B = Sum180.Sum180(A, C)
        b = SinRelSide.SinRelSide(c, C, B)
        a = SinRelSide.SinRelSide(c, C, A)

    else:
        print("Trekanten kan ikke løses sådan.")

    return print("a = "+str(a), "b = "+str(b), "c = "+str(c), "A = "+str(A), "B = "+str(B), "C = "+str(C))
