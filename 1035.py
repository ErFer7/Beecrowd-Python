# -*- coding: utf-8 -*-

val = input().split()

a = int(val[0])
b = int(val[1])
c = int(val[2])
d = int(val[3])

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:

    print("Valores aceitos")
else:

    print("Valores nao aceitos")