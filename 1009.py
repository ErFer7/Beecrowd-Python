# -*- coding: utf-8 -*-

name = input()
fixedSalary = float(input())
selledProducts = float(input())

print("TOTAL = R$ %.2f" % (fixedSalary + (selledProducts * 0.15)))