# -*- coding: utf-8 -*-

from math import sqrt

n = int(input())

for i in range(n):

    nB = int(input())
    wBX, wBY = 0, 0

    for j in range(nB + 1):

        xy = list(map(int, input().split()))

        if j == 0:

            wBX = xy[0]
            wBY = xy[1]
        else:

            if sqrt()