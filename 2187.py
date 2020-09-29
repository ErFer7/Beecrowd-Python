# -*- coding: utf-8 -*-

test = 0

while True:

    test += 1

    value = int(input())

    if value == 0:
        break

    notes_50 = value // 50
    value -= 50 * notes_50

    notes_10 = value // 10
    value -= 10 * notes_10

    notes_5 = value // 5
    value -= 5 * notes_5

    notes_1 = value

    print("Teste %d" % test)
    print("%d %d %d %d" % (notes_50, notes_10, notes_5, notes_1))
    print("")