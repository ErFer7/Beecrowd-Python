# -*- coding: utf-8 -*-

dp = {}
de = {}
dm = {}

n = int(input())

for _ in range(n):

    ln = input().split()

    dp[ln[0]] = int(ln[1])
    de[ln[0]] = int(ln[2])
    dm[ln[0]] = int(ln[3])

# Agrupar os enpatados

if list(dp.values()).count(max(list(dp.values()))) == 1:

    print(list(dp.keys())[list(dp.values()).index(max(list(dp.values())))])
elif list(de.values()).count(max(list(de.values()))) == 1:

    print(list(de.keys())[list(de.values()).index(max(list(de.values())))])
else:

    print(list(dm.keys())[list(dm.values()).index(min(list(dm.values())))])