# -*- coding: utf-8 -*-

nStr = input().split()
nMap = map(float, nStr)
nLst = list(nMap)

if nLst[0] + nLst[1] > nLst[2] and nLst[0] + nLst[2] > nLst[1] and nLst[1] + nLst[2] > nLst[0]:

    print("Perimetro = %.1f" % sum(nLst))
else:

    print("Area = %.1f" % (((nLst[0] + nLst[1]) * nLst[2]) / 2.0))