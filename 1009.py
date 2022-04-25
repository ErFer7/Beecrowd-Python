# -*- coding: utf-8 -*-

'''
Salário com Bônus
'''

name = input()
fixedSalary = float(input())
selledProducts = float(input())

print(f"TOTAL = R$ {(fixedSalary + (selledProducts * 0.15)):.2f}")
