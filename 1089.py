# -*- coding: utf-8 -*-

while True:

    peakCount = 0
    nS = int(input())

    if nS == 0:
        break

    cNLst = list(map(int, input().split()))[:nS]

    for i in range(nS):

        if i == 0:

            if cNLst[nS - 1] > cNLst[i] and cNLst[i] < cNLst[i + 1]:

                peakCount += 1
            elif cNLst[nS - 1] < cNLst[i] and cNLst[i] > cNLst[i + 1]:

                peakCount += 1
        elif i == nS - 1:

            if cNLst[i - 1] > cNLst[i] and cNLst[i] < cNLst[0]:

                peakCount += 1
            elif cNLst[i - 1] < cNLst[i] and cNLst[i] > cNLst[0]:
        
                peakCount += 1
        else:

            if cNLst[i - 1] > cNLst[i] and cNLst[i] < cNLst[i + 1]:

                peakCount += 1
            elif cNLst[i - 1] < cNLst[i] and cNLst[i] > cNLst[i + 1]:

                peakCount += 1

    print(peakCount)