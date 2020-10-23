# -*- coding: utf-8 -*-

while True:

    nC = int(input())
    a = ["A", "B", "C", "D", "E"]

    if nC == 0:
        break

    for i in range(nC):

        marked = -1
        valid = False

        nLst = list(map(int, input().split()))

        for i in nLst:

            if i <= 127:

                if marked == -1:

                    marked = nLst.index(i)
                    valid = True
                else:

                    valid = False
        
        if valid:

            print(a[marked])
        else:

            print("*")