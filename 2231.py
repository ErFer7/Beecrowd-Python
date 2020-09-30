# -*- coding: utf-8 -*-

# NOTA: Não pensei em uma implementação que não usasse vetores

count = 0

while True:

    count += 1

    tLst = []
    tMMin = 250.0
    tMMax = -250.0

    nm = list(map(int, input().split()))

    if nm[0] == 0 and nm[1] == 0:
        break

    for i in range(nm[0]):

        t = float(input())

        tLst.append(t)
    
    for i in range(nm[0] - (nm[1] - 1)):

        mT = 0

        for j in range(nm[1]):

            mT += tLst[j + i] / nm[1]

        if mT > tMMax:

            tMMax = mT
        
        if mT < tMMin:

            tMMin = mT
        
    print("Teste {0}".format(count))
    print("{0} {1}\n".format(int(tMMin), int(tMMax)))