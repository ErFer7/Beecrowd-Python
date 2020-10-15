# -*- coding: utf-8 -*-

n, m = map(int, input().split())

r = [0] * n

for _ in range(m):

    p, d = map(int, input().split())
    
    r[p - 1] = 1

    nD = 0

    while True:
        
        nD += 1

        if p + d * nD - 1 < n:

            r[p + d * nD - 1] = 1
        else:

            nD = 0
            break
    
    while True:

        nD += 1

        if p - d * nD - 1 >= 0:

            r[p - d * nD - 1] = 1
        else:

            break

for i in r:

    print(i)