# -*- coding: utf-8 -*-

count = 0

while True:

    count += 1
    
    n = int(input())

    if n == 0:
        break

    i, j, s, maxI, maxJ, maxS = 0, 0, 0, 0, 0, 0

    for k in range(n):

        x, y = map(int, input().split())

        s += x - y

        if s > 0:

            if i == 0:

                i = k + 1

            j = k + 1
        else:

            s, i, j = 0, 0, 0
        
        if s >= maxS:

            maxS = s
            maxI = i
            maxJ = j

    print("Teste {0}".format(count))

    if maxI > 0 and maxJ > 0:

        print("{0} {1}\n".format(maxI, maxJ))
    else:

        print("nenhum\n")