# -*- coding: utf-8 -*-

n = int(input())
nStr = input().split()
nMap = map(int, nStr)
nLst = list(nMap)

nCLst = nLst[:n]

print("Menor valor: %d" % min(nCLst))
print("Posicao: %d" % nCLst.index(min(nCLst)))