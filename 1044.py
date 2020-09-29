# -*- coding: utf-8 -*-

nStr = input().split()
nMap = map(int, nStr)
nLst = list(nMap)

if nLst[0] % nLst[1] == 0 or nLst[1] % nLst[0] == 0:

    print("Sao Multiplos")
else:

    print("Nao sao Multiplos")