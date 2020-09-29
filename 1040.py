# -*- coding: utf-8 -*-

wLst = [2.0, 3.0, 4.0, 1.0]

gStr = input().split()
gMap = map(float, gStr)
gLst = list(gMap)

average = round((gLst[0] * wLst[0] + gLst[1] * wLst[1] + gLst[2] * wLst[2] + gLst[3] * wLst[3]) / sum(wLst), 1)

print("Media: %.1f" % average)

if average >= 7.0:

    print("Aluno aprovado.")
elif average >= 5.0:

    print("Aluno em exame.")

    gR = float(input())

    print("Nota do exame: %.1f" % gR)

    recAverage = round((gR + average) / 2.0, 1)

    if recAverage >= 5.0:

        print("Aluno aprovado.")
    else:

        print("Aluno reprovado.")

    print("Media final: %.1f" % recAverage)
else:

    print("Aluno reprovado.")