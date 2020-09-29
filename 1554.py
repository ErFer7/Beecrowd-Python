# -*- coding: utf-8 -*-

from math import sqrt

n = int(input())

for i in range(n):

    nB = int(input())
    wBX, wBY = 0.0, 0.0
    dMin = 3200.0
    iP = 0

    for j in range(nB + 1):

        xy = list(map(float, input().split()))

        if j == 0:

            wBX = xy[0]
            wBY = xy[1]
        else:

            d = sqrt((xy[0] - wBX)**2 + (xy[1] - wBY)**2)

            if d < dMin:

                dMin = d
                iP = j
    
    print(iP)