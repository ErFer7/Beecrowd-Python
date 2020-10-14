# -*- coding: utf-8 -*-

pi = 3.14159

a, b, c = map(float, input().split())

print("TRIANGULO: %.3f" % ((a * c) / 2.0))
print("CIRCULO: %.3f" % (pi * c**2))
print("TRAPEZIO: %.3f" % (((a + b) * c) / 2.0))
print("QUADRADO: %.3f" % (b**2))
print("RETANGULO: %.3f" % (a * b))