"""
11. Crie um algoritmo que receba o valor de x, e exiba o valor de f(x), onde:
"""

x = float(input('Valor de x: '))
fx = 0

if x <= 1:
    fx = 1
if 1 < x <= 2:
    fx = 2
if 2 < x <= 3:
    fx = x ** 2
if x > 3:
    fx = x ** 3

print(f'Valor de f(x): {fx}')
